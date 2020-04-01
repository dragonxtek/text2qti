# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Geoffrey M. Poore
# All rights reserved.
#
# Licensed under the BSD 3-Clause License:
# http://opensource.org/licenses/BSD-3-Clause
#


import datetime
from typing import Optional


TEMPLATE = '''\
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{manifest_identifier}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 http://www.imsglobal.org/xsd/imsmd_v1p2p2.xsd">
  <metadata>
    <schema>IMS Content</schema>
    <schemaversion>1.1.3</schemaversion>
    <imsmd:lom>
      <imsmd:general>
        <imsmd:title>
          <imsmd:string>QTI assessment generated by text2qti</imsmd:string>
        </imsmd:title>
      </imsmd:general>
      <imsmd:lifeCycle>
        <imsmd:contribute>
          <imsmd:date>
            <imsmd:dateTime>{date}</imsmd:dateTime>
          </imsmd:date>
        </imsmd:contribute>
      </imsmd:lifeCycle>
      <imsmd:rights>
        <imsmd:copyrightAndOtherRestrictions>
          <imsmd:value>yes</imsmd:value>
        </imsmd:copyrightAndOtherRestrictions>
        <imsmd:description>
          <imsmd:string>Private (Copyrighted) - http://en.wikipedia.org/wiki/Copyright</imsmd:string>
        </imsmd:description>
      </imsmd:rights>
    </imsmd:lom>
  </metadata>
  <organizations/>
  <resources>
    <resource identifier="{assessment_identifier}" type="imsqti_xmlv1p2">
      <file href="{assessment_identifier}/{assessment_identifier}.xml"/>
      <dependency identifierref="{dependency_identifier}"/>
    </resource>
    <resource identifier="{dependency_identifier}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{assessment_identifier}/assessment_meta.xml">
      <file href="{assessment_identifier}/assessment_meta.xml"/>
    </resource>
  </resources>
</manifest>
'''


def imsmanifest(*,
                manifest_identifier: str,
                assessment_identifier: str,
                dependency_identifier: str,
                date: Optional[str]=None) -> str:
    '''
    Generate `imsmanifest.xml`.
    '''
    if date is None:
        date = str(datetime.date.today())
    return TEMPLATE.format(manifest_identifier=manifest_identifier,
                           assessment_identifier=assessment_identifier,
                           dependency_identifier=dependency_identifier,
                           date=date)
