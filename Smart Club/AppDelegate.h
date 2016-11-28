//
//  AppDelegate.h
//  Smart Club
//
//  Created by Meg Grasse on 5/17/16.
//  Copyright © 2016 Meg Grasse. All rights reserved.
//

#import <UIKit/UIKit.h>

#import <EstimoteSDK/EstimoteSDK.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate, ESTBeaconManagerDelegate>

@property (strong, nonatomic) UIWindow *window;
@property (nonatomic) ESTBeaconManager *beaconManager;

-  (NSString *)sendDataTo:(NSString *)endpoint;

@end

