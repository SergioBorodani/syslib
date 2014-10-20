# coding: utf-8
import simplejson as json
from ru.curs.celesta.showcase.utils import XMLJSONConverter

def datapanel(context, main=None, session=None):
    u'''Продедура возвращает информационную панель для разрешений'''
    data = {"datapanel":{"tab":[{"@id":1,
                                "@name":u"Разрешения на таблицы",
                                "element":[{"@id":"permFilter",
                                            "@type":"xforms",
                                            "@template": "security/permissionsFilter.xml",
                                            "@proc":"security.xform.permissionsFilter.cardData.celesta"
                                            },
                                           {"@id":"permGrid",
                                            "@type":"grid",
                                            "@subtype":"JS_LIVE_GRID",
                                            "@plugin":"liveDGrid",
                                            "@proc":"security.grid.permissions.gridData.celesta",
                                            "@hideOnLoad":"true",
                                            "proc":[{"@id":"permGridMeta",
                                                     "@name":"security.grid.permissions.gridMeta.celesta",
                                                     "@type":"METADATA"
                                                     },
                                                    {"@id":"permGridToolBar",
                                                     "@name":"security.grid.permissions.gridToolBar.celesta",
                                                     "@type":"TOOLBAR"
                                                     }],
                                            "related":{"@id":"permFilter"}
                                            },
                                           {"@id":"permXforms",
                                            "@type":"xforms",
                                            "@template": "security/permissions.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.permissions.cardData.celesta",
                                            "proc":{"@id":"permXformSave",
                                                    "@name":"security.xform.permissions.cardDataSave.celesta",
                                                    "@type":"SAVE"},
                                            "related":[{"@id":"permGrid"},
                                                       {"@id":"permFilter"}]
                                            },
                                           {"@id":"permXformDelete",
                                            "@type":"xforms",
                                            "@template":"security/delete.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.permissionsDelete.cardData.celesta",
                                            "proc":{"@id":"permXformSave",
                                                    "@name":"security.xform.permissionsDelete.cardDelete.celesta",
                                                    "@type":"SAVE"},
                                            "related":{"@id":"permGrid"}
                                            },
                                           {"@id":"permDownloadXform",
                                            "@type":"xforms",
                                            "@template":"security/tableLoad.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.permissionsLoad.cardData.celesta",
                                            "proc":{"@id":"tableXformDownload",
                                                    "@name":"security.xform.permissionsLoad.permissionsDownload.celesta",
                                                    "@type":"DOWNLOAD"}
                                             },
                                            {"@id":"permUploadXform",
                                             "@type":"xforms",
                                             "@template":"security/tableLoad.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.permissionsLoad.cardData.celesta",
                                             "proc":[{"@id":"tableXformUpload",
                                                      "@name":"security.xform.permissionsLoad.permissionsUpload.celesta",
                                                      "@type":"UPLOAD"},
                                                     {"@id":"permissionsXformUploadSave",
                                                      "@name":"security.xform.permissionsLoad.cardSave.celesta",
                                                      "@type":"SAVE"}
                                                     ]
                                             }
                                           
#                                           ,{"@id":"permGrid222",
#                                            "@type":"grid",
#                                            "@subtype":"JS_LIVE_GRID",
#                                            "@plugin":"liveDGrid",
#                                            "@proc":"security.grid.permissions.gridData.celesta",
#                                            "@hideOnLoad":"true",
#                                            "proc":[{"@id":"permGridMeta",
#                                                     "@name":"security.grid.permissions.gridMeta.celesta",
#                                                     "@type":"METADATA"
#                                                     },
#                                                    {"@id":"permGridToolBar",
#                                                     "@name":"security.grid.permissions.gridToolBar.celesta",
#                                                     "@type":"TOOLBAR"
#                                                     }],
#                                            "related":{"@id":"permFilter"}
#                                            }
                                           
                                           ]
                                },
                                {"@id":2,
                                 "@name":u"Прочие разрешения",
                                 "element":[{"@id":"customPermFilter",
                                             "@type":"xforms",
                                             "@template": "security/customPermissionsFilter.xml",
                                             "@proc":"security.xform.customPermissionsFilter.cardData.celesta"
                                             },
                                            {"@id":"customPermissionsGrid",
                                             "@type":"grid",
                                             "@subtype":"JS_LIVE_GRID",
                                             "@plugin":"liveDGrid",
                                             "@proc":"security.grid.customPermissions.gridData.celesta",
                                             "@hideOnLoad":"true",
                                             "proc":[{"@id":"customPermissionsGridMeta",
                                                      "@name":"security.grid.customPermissions.gridMeta.celesta",
                                                      "@type":"METADATA"
                                                      },
                                                     {"@id":"customPermissionsGridToolBar",
                                                      "@name":"security.grid.customPermissions.gridToolBar.celesta",
                                                      "@type":"TOOLBAR"
                                                      }],
                                             "related":{"@id":"customPermFilter"}
                                             },
                                            {"@id":"customPermissionsXforms",
                                             "@type":"xforms",
                                             "@template": "security/customPermissions.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.customPermissions.cardData.celesta",
                                             "proc":{"@id":"customPermissionsXformSave",
                                                     "@name":"security.xform.customPermissions.cardDataSave.celesta",
                                                     "@type":"SAVE"},
                                             "related":[{"@id":"customPermissionsGrid"},
                                                        {"@id":"customPermFilter"}]
                                             },
                                            {"@id":"customPermissionsXformDelete",
                                             "@type":"xforms",
                                             "@template":"security/delete.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.customPermissionsDelete.cardData.celesta",
                                             "proc":{"@id":"customPermissionsXformDelete",
                                                     "@name":"security.xform.customPermissionsDelete.cardDelete.celesta",
                                                     "@type":"SAVE"},
                                             "related":{"@id":"customPermissionsGrid"}
                                             },
                                            {"@id":"customPermissionsDownloadXform",
                                            "@type":"xforms",
                                            "@template":"security/tableLoad.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.customPermissionsLoad.cardData.celesta",
                                            "proc":{"@id":"tableXformDownload",
                                                    "@name":"security.xform.customPermissionsLoad.permissionsDownload.celesta",
                                                    "@type":"DOWNLOAD"}
                                             },
                                            {"@id":"customPermissionsUploadXform",
                                             "@type":"xforms",
                                             "@template":"security/tableLoad.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.customPermissionsLoad.cardData.celesta",
                                             "proc":[{"@id":"tableXformUpload",
                                                      "@name":"security.xform.customPermissionsLoad.permissionsUpload.celesta",
                                                      "@type":"UPLOAD"},
                                                     {"@id":"customPermissionsXformUploadSave",
                                                      "@name":"security.xform.customPermissionsLoad.cardSave.celesta",
                                                      "@type":"SAVE"}
                                                     ]
                                             },
                                            {"@id":"rolesCustomPermissionsGrid",
                                             "@type":"grid",
                                             "@subtype":"JS_LIVE_GRID",
                                             "@plugin":"liveDGrid",
                                             "@proc":"security.grid.rolesCustomPermissions.gridData.celesta",
                                             "@hideOnLoad":"true",
                                             "proc":[{"@id":"rolesCustomPermissionsGridMeta",
                                                      "@name":"security.grid.rolesCustomPermissions.gridMeta.celesta",
                                                      "@type":"METADATA"
                                                      },
                                                     {"@id":"rolesCustomPermissionsGridToolBar",
                                                      "@name":"security.grid.rolesCustomPermissions.gridToolBar.celesta",
                                                      "@type":"TOOLBAR"
                                                      }],
                                             "related":{"@id":"customPermissionsGrid"}
                                             },
                                            {"@id":"rolesCustomPermissionsXforms",
                                             "@type":"xforms",
                                             "@template": "security/rolesCustomPermissions.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.rolesCustomPermissions.cardData.celesta",
                                             "proc":{"@id":"rolesCustomPermissionsXformSave",
                                                     "@name":"security.xform.rolesCustomPermissions.cardDataSave.celesta",
                                                     "@type":"SAVE"},
                                             "related":[{"@id":"customPermissionsGrid"},
                                                        {"@id":"rolesCustomPermissionsGrid"}]
                                             },
                                            {"@id":"rolesCustomPermissionsXformDelete",
                                             "@type":"xforms",
                                             "@template":"security/delete.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.rolesCustomPermissionsDelete.cardData.celesta",
                                             "proc":{"@id":"rolesCustomPermissionsXformDelete",
                                                     "@name":"security.xform.rolesCustomPermissionsDelete.cardDelete.celesta",
                                                     "@type":"SAVE"},
                                             "related":[{"@id":"customPermissionsGrid"},
                                                        {"@id":"rolesCustomPermissionsGrid"}]
                                             },
                                            {"@id":"rolesCustomPermissionsDownloadXform",
                                             "@type":"xforms",
                                             "@template":"security/tableLoad.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.rolesCustomPermissionsLoad.cardData.celesta",
                                             "proc":{"@id":"tableXformDownload",
                                                     "@name":"security.xform.rolesCustomPermissionsLoad.rolesPermissionsDownload.celesta",
                                                     "@type":"DOWNLOAD"}
                                             },
                                            {"@id":"rolesCustomPermissionsUploadXform",
                                             "@type":"xforms",
                                             "@template":"security/tableLoad.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.rolesCustomPermissionsLoad.cardData.celesta",
                                             "proc":[{"@id":"tableXformUpload",
                                                      "@name":"security.xform.rolesCustomPermissionsLoad.rolesPermissionsUpload.celesta",
                                                      "@type":"UPLOAD"},
                                                     {"@id":"rolesCustomPermissionsXformUploadSave",
                                                      "@name":"security.xform.rolesCustomPermissionsLoad.cardSave.celesta",
                                                      "@type":"SAVE"}
                                                     ]
                                             }]
                                 },
                                {"@id":3,
                                 "@name":u"Типы разрешений",
                                 "element":[{"@id":"customPermissionsTypesGrid",
                                            "@type":"grid",
                                            "@subtype":"JS_LIVE_GRID",
                                            "@plugin":"liveDGrid",
                                            "@proc":"security.grid.customPermissionsTypes.gridData.celesta",
                                            "proc":[{"@id":"customPermissionsTypesGridMeta",
                                                     "@name":"security.grid.customPermissionsTypes.gridMeta.celesta",
                                                     "@type":"METADATA"
                                                     },
                                                    {"@id":"customPermissionsTypesGridToolBar",
                                                     "@name":"security.grid.customPermissionsTypes.gridToolBar.celesta",
                                                     "@type":"TOOLBAR"
                                                     }]
                                            },
                                           {"@id":"customPermissionsTypesXforms",
                                            "@type":"xforms",
                                            "@template": "security/customPermissionsTypes.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.customPermissionsTypes.cardData.celesta",
                                            "proc":{"@id":"customPermissionsTypesXformSave",
                                                    "@name":"security.xform.customPermissionsTypes.cardDataSave.celesta",
                                                    "@type":"SAVE"},
                                            "related":{"@id":"customPermissionsTypesGrid"}
                                            },
                                           {"@id":"customPermissionsTypesXformDelete",
                                            "@type":"xforms",
                                            "@template":"security/delete.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.customPermissionsTypesDelete.cardData.celesta",
                                            "proc":{"@id":"customPermissionsTypesXformDelete",
                                                    "@name":"security.xform.customPermissionsTypesDelete.cardDelete.celesta",
                                                    "@type":"SAVE"},
                                            "related":{"@id":"customPermissionsTypesGrid"}
                                            },
                                            {"@id":"customPermissionsTypesDownloadXform",
                                            "@type":"xforms",
                                            "@template":"security/tableLoad.xml",
                                            "@neverShowInPanel":"true",
                                            "@proc":"security.xform.customPermissionsTypesLoad.cardData.celesta",
                                            "proc":{"@id":"tableXformDownload",
                                                    "@name":"security.xform.customPermissionsTypesLoad.permissionsTypesDownload.celesta",
                                                    "@type":"DOWNLOAD"}
                                             },
                                            {"@id":"customPermissionsTypesUploadXform",
                                             "@type":"xforms",
                                             "@template":"security/tableLoad.xml",
                                             "@neverShowInPanel":"true",
                                             "@proc":"security.xform.customPermissionsTypesLoad.cardData.celesta",
                                             "proc":[{"@id":"tableXformUpload",
                                                      "@name":"security.xform.customPermissionsTypesLoad.permissionsTypesUpload.celesta",
                                                      "@type":"UPLOAD"},
                                                     {"@id":"customPermissionsTypesXformUploadSave",
                                                      "@name":"security.xform.customPermissionsTypesLoad.cardSave.celesta",
                                                      "@type":"SAVE"}
                                                     ]
                                             }]
                                 }]
                         }
            }    
    #raise Exception(XMLJSONConverter(input=data).parse())
    return XMLJSONConverter.jsonToXml(json.dumps(data))

