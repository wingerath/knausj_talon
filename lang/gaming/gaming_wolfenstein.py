from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gamingwolfenstein
mode: command 
and code.language: gamingwolfenstein
"""
