from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gaming_Wolfenstein
mode: command 
and code.language: gaming_Wolfenstein
"""
