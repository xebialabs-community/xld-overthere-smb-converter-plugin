#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
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