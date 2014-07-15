# -*- coding: utf-8 -*-
"""
/***************************************************************************
 selenext
                                 A QGIS plugin
 selenext
                             -------------------
        begin                : 2014-07-15
        copyright            : (C) 2014 by geodrinx
        email                : geodrinx@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load selenext class from file selenext.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .selenext import selenext
    return selenext(iface)
