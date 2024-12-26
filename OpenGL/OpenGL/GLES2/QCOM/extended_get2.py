'''OpenGL extension QCOM.extended_get2

This module customises the behaviour of the 
OpenGL.raw.GLES2.QCOM.extended_get2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables instrumenting the driver for debugging of OpenGL ES 
	applications.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/extended_get2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.QCOM.extended_get2 import *
from OpenGL.raw.GLES2.QCOM.extended_get2 import _EXTENSION_NAME

def glInitExtendedGet2QCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glExtGetShadersQCOM.shaders size not checked against maxShaders
glExtGetShadersQCOM=wrapper.wrapper(glExtGetShadersQCOM).setInputArraySize(
    'numShaders', 1
).setInputArraySize(
    'shaders', None
)
# INPUT glExtGetProgramsQCOM.programs size not checked against maxPrograms
glExtGetProgramsQCOM=wrapper.wrapper(glExtGetProgramsQCOM).setInputArraySize(
    'numPrograms', 1
).setInputArraySize(
    'programs', None
)
### END AUTOGENERATED SECTION