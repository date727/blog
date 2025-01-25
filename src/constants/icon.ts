import type { Favicon } from '@/types/config.ts'

export const defaultFavicons: Favicon[] = [
	{
       src: '/favicon/favicon.png',    // Path of the favicon, relative to the /public directory
       theme: 'light',
	   sizes: '32x32',              // (Optional) Size of the favicon, set only if you have favicons of different sizes
    },
	{
		src:'/favicon/favicon2.png',
		theme:'dark',
		sizes: '32x32',
	},
]
