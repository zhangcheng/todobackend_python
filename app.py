#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from todobackend.web_app.app import create_app

if __name__ == "__main__":
    create_app().run(debug=True, threaded=True)
