#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# Set the variables
srcID = thisCi.id
srcType = thisCi.type

#Determine where to transform to
if srcType == 'overthere.AliasSmbHost':
	targetType = 'overthere.AliasCifsHost'
	propertyKey = 'cifsPort'
	propertyValue = thisCi.getProperty('smbPort')

elif srcType == 'overthere.AliasCifsHost':
	targetType = 'overthere.AliasSmbHost'
	propertyKey = 'smbPort'
	propertyValue = thisCi.getProperty('cifsPort')

elif srcType == 'overthere.SmbHost':
	targetType = 'overthere.CifsHost'
	propertyKey = 'cifsPort'
	propertyValue = thisCi.getProperty('smbPort')

elif srcType == 'overthere.CifsHost':
	targetType = 'overthere.SmbHost'
	propertyKey = 'smbPort'
	propertyValue = thisCi.getProperty('cifsPort')

#Get the current CI, set the Type, copy port setting, and update the repository
srcCI = repositoryService.read(srcID)
srcCI.setType(Type.valueOf(targetType))
srcCI.setProperty(propertyKey, propertyValue)
repositoryService.update(srcID, srcCI)
