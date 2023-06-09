{
  "targets": [
    {
			"target_name": "addon_webview",
			"cflags!": [ "-fno-exceptions" ],
			"cflags_cc!": [
    		"-fno-exceptions",
 				"-std=c++11",
				"-Iwebview.h"
      ],
			"sources": [ "addon_webview.cc" ],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/WebKit.framework',
        ] 
			}
		}
  ]
}
