import UIKit
import Capacitor

/// Registers the local WidgetBridge plugin (Capacitor 6/7 local-plugin pattern).
/// In Main.storyboard set the Bridge View Controller's custom class to MyViewController (module: App).
class MyViewController: CAPBridgeViewController {
    override open func capacitorDidLoad() {
        bridge?.registerPluginInstance(WidgetBridgePlugin())
    }
}
