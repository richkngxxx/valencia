import UIKit

// iOS 27 SDK requires the UIScene lifecycle. With a storyboard
// (UISceneStoryboardFile = Main in Info.plist) UIKit builds the window
// and Capacitor's bridge view controller itself; we only need the delegate.
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
}
