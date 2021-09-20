#!/usr/bin/env python

import greetings

def test_greeting():
    assert greetings.say_hi("Greta") == "Hello world! says Greta"

def test_byebye():
    assert greetings.say_bye("Agnes") == "Goodbye Agnes"