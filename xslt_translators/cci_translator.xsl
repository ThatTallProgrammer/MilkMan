<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:d="http://iase.disa.mil/cci">
    <xsl:output method="xml" encoding="UTF-8"/>
    <xsl:template match="/">
        <cci_items>
            <xsl:for-each select="d:cci_list/d:cci_items/d:cci_item">
                <cci_item>
                    <xsl:attribute name="id">
                        <xsl:value-of select="@id"/>
                    </xsl:attribute>
                    <xsl:attribute name="status">
                        <xsl:value-of select="d:status"/>
                    </xsl:attribute>
                    <xsl:attribute name="publishdate">
                        <xsl:value-of select="d:publishdate"/>
                    </xsl:attribute>
                    <xsl:attribute name="contributor">
                        <xsl:value-of select="d:contributor"/>
                    </xsl:attribute>
                    <xsl:attribute name="definition">
                        <xsl:value-of select="d:definition"/>
                    </xsl:attribute>
                    <xsl:attribute name="type">
                        <xsl:value-of select="d:type"/>
                    </xsl:attribute>
                    <xsl:attribute name="parameter">
                        <xsl:value-of select="d:parameter"/>
                    </xsl:attribute>
                    <xsl:attribute name="note">
                        <xsl:value-of select="d:note"/>
                    </xsl:attribute>
                    <references>
                        <xsl:for-each select="d:references/d:reference">
                            <reference>
                                <xsl:attribute name="creator">
                                    <xsl:value-of select="@creator"/>
                                </xsl:attribute>
                                <xsl:attribute name="title">
                                    <xsl:value-of select="@title"/>
                                </xsl:attribute>
                                <xsl:attribute name="version">
                                    <xsl:value-of select="@version"/>
                                </xsl:attribute>
                                <xsl:attribute name="location">
                                    <xsl:value-of select="@location"/>
                                </xsl:attribute>
                                <xsl:attribute name="index">
                                    <xsl:value-of select="@index"/>
                                </xsl:attribute>
                            </reference>
                        </xsl:for-each>
                    </references>
                </cci_item>
            </xsl:for-each>
        </cci_items>
    </xsl:template>
</xsl:stylesheet>