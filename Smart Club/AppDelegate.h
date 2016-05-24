//
//  AppDelegate.h
//  Smart Club
//
//  Created by Meg Grasse on 5/17/16.
//  Copyright © 2016 Meg Grasse. All rights reserved.
//

#import <UIKit/UIKit.h>

#import <SocialRetailSRSDK/SRBeaconDelegate.h>
#import <SocialRetailSRSDK/SRBeaconManager.h>
#import <SocialRetailSRSDK/SRWebViewController.h>

//@interface AppDelegate : NSObject <UIApplicationDelegate,SRBeaconDelegate>
@interface AppDelegate : UIResponder <UIApplicationDelegate,SRBeaconDelegate>

@property (strong, nonatomic) UIWindow *window;


@end

