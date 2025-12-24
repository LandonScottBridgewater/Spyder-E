# -----------------------------------------------------------------------------
# Copyright (c) 2017- Spyder Project Contributors
#
# Released under the terms of the MIT License
# (see LICENSE.txt in the project root directory for details)
# -----------------------------------------------------------------------------

"""
Deprecated aliases of classes in :mod:`spyder_e.plugins.editor.api`.

.. deprecated:: 6.2

    This module will issue a :exc:`DeprecationWarning` in Spyder 6.2 and
    be removed in Spyder 7.0, as with the migration of the :guilabel:`Editor`
    to the new plugin API these classes have been canonically accessed
    directly from the Editor plugin since Spyder 6.0.

    Use :class:`spyder_e.plugins.editor.api.editorextension.EditorExtension`
    and :class:`spyder_e.plugins.editor.api.panel.Panel` instead.
"""

from spyder_e.plugins.editor.api.editorextension import EditorExtension
from spyder_e.plugins.editor.api.panel import Panel


__all__ = ["EditorExtension", "Panel"]
