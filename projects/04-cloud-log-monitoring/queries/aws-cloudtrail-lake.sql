-- Root account activity
SELECT eventTime, eventName, sourceIPAddress, userIdentity.type, userIdentity.arn
FROM $EDS
WHERE userIdentity.type = 'Root'
ORDER BY eventTime DESC;

-- Failed console logins
SELECT eventTime, sourceIPAddress, userAgent, errorMessage, userIdentity.accountId
FROM $EDS
WHERE eventName = 'ConsoleLogin'
  AND responseElements.ConsoleLogin = 'Failure'
ORDER BY eventTime DESC;

-- New administrative policy attachment
SELECT eventTime, eventName, sourceIPAddress, userIdentity.arn, requestParameters.policyArn, requestParameters.userName, requestParameters.roleName
FROM $EDS
WHERE eventName IN ('AttachUserPolicy', 'AttachRolePolicy', 'PutUserPolicy', 'PutRolePolicy')
ORDER BY eventTime DESC;

-- Security group opened broadly
SELECT eventTime, eventName, userIdentity.arn, sourceIPAddress, requestParameters
FROM $EDS
WHERE eventName IN ('AuthorizeSecurityGroupIngress', 'ModifySecurityGroupRules')
  AND requestParameters LIKE '%0.0.0.0/0%'
ORDER BY eventTime DESC;
