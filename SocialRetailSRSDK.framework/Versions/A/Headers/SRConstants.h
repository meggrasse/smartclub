//
//  constants.h
//  iBeaconTest
//
//  Created by Eliel Cohen on 30/10/14.
//  Copyright (c) 2014 Digital Social Retail. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface SRConstants : NSObject

FOUNDATION_EXPORT NSString *const defaultUrl;
FOUNDATION_EXPORT NSString *const webServiceUrl;
FOUNDATION_EXPORT NSString *const beaconUrl;

FOUNDATION_EXPORT NSString *const beaconUUIDStringStr;
FOUNDATION_EXPORT NSString *const regionIdentifier;

FOUNDATION_EXPORT NSString *const beaconUUIDStringSecond;
FOUNDATION_EXPORT NSString *const regionIdentifierSecond;

FOUNDATION_EXPORT float const min_interval;
FOUNDATION_EXPORT float const max_distance;
//FOUNDATION_EXPORT NSString *const urlAds;

//FOUNDATION_EXPORT NSString *const beaconUUIDStringT;
FOUNDATION_EXPORT NSString *const regionIdentifierT;

@end
