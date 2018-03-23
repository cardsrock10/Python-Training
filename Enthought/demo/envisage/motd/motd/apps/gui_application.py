"""
Envisage GUI Application
------------------------

This class handles the life-cycle of a Pyface GUI.  Plugins can
display windows via mechinisms such as edit_traits().

This is intended to be a very simple shell for lifting an existing
pure TraitsUI or Pyface (or even Qt) app into an Envisage app.

More sophisticated applications should use Tasks.

"""

from traits.api import Event, Supports
from envisage.api import Application


class GUIApplication(Application):
    """ The entry point for an Envisage GUI application.

    This class handles the life-cycle of a Pyface GUI.  Plugins can
    display windows via mechinisms such as edit_traits().
    
    This is intended to be a very simple shell for lifting an existing
    pure TraitsUI or Pyface (or even Qt) app into an Envisage app.
    
    More sophisticated applications should use Tasks.
    
    """

    #### 'GUIApplication' interface #########################################

    #: The PyFace GUI for the application.
    gui = Supports('pyface.i_gui.IGUI')

    #: The splash screen for the application. By default, there is no splash
    #: screen.
    splash_screen = Supports('pyface.i_splash_screen.ISplashScreen')

    #### Application lifecycle events #########################################

    # Fired after the GUI event loop has been started.
    application_initialized = Event

    ###########################################################################
    # 'IApplication' interface.
    ###########################################################################

    def run(self):
        """ Run the application.

        Returns:
        --------
        Whether the application started successfully (i.e., without a veto).
        
        """
        
        # Make sure the GUI has been created (so that, if required, the splash
        # screen is shown).
        gui = self.gui

        started = self.start()
        if started:
            # Start the GUI event loop.
            gui.set_trait_later(self, 'application_initialized', self)
            gui.start_event_loop()
            
            # the application blocks here...
            self.stop()

        return started

    #### Trait initializers ###################################################

    def _gui_default(self):
        from pyface.api import GUI
        return GUI(splash_screen=self.splash_screen)
