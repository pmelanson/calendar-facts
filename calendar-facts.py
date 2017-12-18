#!/usr/bin/env python3

"""
calendar-facts.py
https://xkcd.com/1930/
by Patrick Melanson
https://github.com/pmelanson/calendar-facts
pj2melan@csclub.uwaterloo.ca
message me if you want to use this i guess
"""

import itertools
import random

DID_YOU_KNOW_THAT = {'Did you know that'}

PHENOMENON = {
    'the Fall equinox',
    'the Spring equinox',
    'the Winter Solstice',
    'the Winter Olympics',
    'the Summer Solstice',
    'the Summer Olympics',
    'the earliest sunrise',
    'the earliest sunset',
    'the latest sunrise',
    'the latest sunset',
    'daylight saving time',
    'daylight savings time',
    'the leap day',
    'the leap year',
    'Easter',
    'the harvest moon',
    'the super moon',
    'the blood moon',
    'Toyota Truck Month',
    'Shark Week',
}

WHAT_HAPPENS = {
    'happens earlier every year',
    'happens later every year',
    'happens at the wrong time every year',
    'drifts out of sync with the sun',
    'drifts out of sync with the moon',
    'drifts out of sync with the Zodiac',
    'drifts out of sync with the Gregorian calendar',
    'drifts out of sync with the Mayan calendar',
    'drifts out of sync with the Lunar calendar',
    'drifts out of sync with the iPhone calendar',
    'drifts out of sync with the atomic clock in Colorado',
    'might not happen this year',
    'might happen twice this year',
}

BECAUSE_OF = {
    'because of'
}

THE_CAUSE = {
    'time zone legislation in Indiana?',
    'time zone legislation in Arizona?',
    'time zone legislation in Russia?',
    'a decree by the Pope in the 1500s?',
    'magnetic field reversal?',
    'an arbitrary decision by Benjamin Franklin?',
    'an arbitrary decision by Isaac Newton?',
    'an arbitrary decision by FDR?',
} | {
    ' of the '.join(each) for each in itertools.product(
        {
            'precession',
            'libration',
            'nutation',
            'libation',
            'eccentricity',
            'obliquity'
        },
        {
            'Moon?',
            'Sun?',
            'Earth\'s axis?',
            'Equator?',
            'Prime Meridian?',
            'International Date Line?',
            'Mason-Dixon Line?'
        }
    )
}

APPARENTLY = {
    'Apparently'
}

CONSEQUENCE = {
    'it causes a predictable increase in car accidents.',
    'that\'s why we have leap seconds.',
    'scientists are really worried.',
    'it was even more extreme during the Bronze Age.',
    'it was even more extreme during the Ice Age.',
    'it was even more extreme during the Cretaceous.',
    'it was even more extreme during the 1990s.',
    'there\'s a proposal to fix it, but it will never happen',
    'there\'s a proposal to fix it, but it actually makes things worse',
    'there\'s a proposal to fix it, but it is stalled in Congress',
    'there\'s a proposal to fix it, but it might be unconstitutional',
    'is getting worse and no one knows why',
}


def main():
    print(' '.join([random.choice(tuple(each)) for each in [
        DID_YOU_KNOW_THAT,
        PHENOMENON,
        WHAT_HAPPENS,
        BECAUSE_OF,
        THE_CAUSE,
        APPARENTLY,
        CONSEQUENCE,
    ]]))


if __name__ == '__main__':
    main()
