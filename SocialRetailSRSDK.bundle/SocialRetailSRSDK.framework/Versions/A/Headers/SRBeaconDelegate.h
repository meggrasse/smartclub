//
//  SRBeaconDelegate.h
//  SocialRetailSDK
//
//  Created by vasi on 18/02/15.
//  Copyright (c) 2015 DigitalSocialRetail. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>
#import "SRWebViewController.h"

@protocol SRBeaconDelegate <NSObject>

-(void)launchLocalNotification:(NSString * ) AlertText withRedirectURL:(NSString*)redirectURL andOutletName:(NSString*)outletName;
//-(void)currentLocationUpd:(CLLocation*)location;
-(void)startBeconDetection;
-(void)showWebViewController:(SRWebViewController*)webViewController;

@end
