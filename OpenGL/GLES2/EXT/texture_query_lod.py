'''OpenGL extension EXT.texture_query_lod

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.texture_query_lod to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds a new set of fragment shader texture functions
	(textureLOD) that return the results of automatic level-of-detail
	computations that would be performed if a texture lookup were performed.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_query_lod.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.texture_query_lod import *
from OpenGL.raw.GLES2.EXT.texture_query_lod import _EXTENSION_NAME

def glInitTextureQueryLodEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION