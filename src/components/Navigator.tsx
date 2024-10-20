'use client';
import { useEffect, useState } from 'react';
import { Tooltip } from '@nextui-org/react';

interface NavigatorProps {
    children: React.ReactNode[] | React.ReactNode;
}

export default function Navigator({ children }: NavigatorProps) {
    const [isMobile, setIsMobile] = useState(false);
    const rem = (a: number) => parseFloat(getComputedStyle(document.documentElement).fontSize) * a;

    useEffect(() => {
        const userAgent = typeof window.navigator === 'undefined' ? '' : navigator.userAgent;
        const mobile = Boolean(
            userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i)
        );
        setIsMobile(mobile);
    }, []);

    const btn1 = (constraints: string) => <Tooltip content="Home" closeDelay={0}><button
        className={`btn btn-ghost btn-square fixed z-50 ${constraints}`}
        onClick={() => window.scroll({ top: 0, behavior: 'smooth' })}
        onMouseEnter={() => { }}
        onMouseLeave={() => { }}
    >
        <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            className="size-6"
        >
            <path
                d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z"
            />
            <path
                d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z"
            />
        </svg>
    </button></Tooltip>

    const btn2 = (constraints: string) => <Tooltip content="About" closeDelay={0}><button
        className={`btn btn-ghost btn-square fixed z-50 ${constraints}`}
        onClick={() => window.scroll({ top: (isMobile) ? window.innerHeight + (rem(4) * 1.2 * 2 * 0) : window.innerHeight, behavior: 'smooth' })}
        onMouseEnter={() => { }}
        onMouseLeave={() => { }}
    >
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            className="size-6"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z"
            />
        </svg>
    </button></Tooltip>

    const btn3 = (constraints: string) => <Tooltip content="Projects" closeDelay={0}><button
        className={`btn btn-ghost btn-square fixed z-50 ${constraints}`}
        onClick={() => window.scroll({ top: (isMobile) ? (window.innerHeight * 2) + (rem(4) * 2.35 * 1.5) : window.innerHeight * 2, behavior: 'smooth' })}
        onMouseEnter={() => { }}
        onMouseLeave={() => { }}
    >
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            className="size-6"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"
            />
        </svg>
    </button></Tooltip>

    return (
        <main>
            {isMobile ? (
                <>
                    <div className="flex flex-row fixed z-40">
                        <div className="w-screen h-16 backdrop-blur-lg"></div>
                        <div className="w-screen"></div>
                    </div>
                    {btn1('top-2 left-2')}
                    {btn2('top-2 left-[43vw]')}
                    {btn3('top-2 right-2')}
                    <div className="pt-16">
                        {children}
                    </div>
                </>
            ) : (
                <>
                    <div className="flex flex-col fixed z-40">
                        <div className="h-screen bg-base-100 w-16"></div>
                        <div className="h-screen"></div>
                    </div>
                    {btn1('left-2 top-4')}
                    {btn2('left-2 top-1/2')}
                    {btn3('left-2 bottom-4')}
                    <div className="pl-16 overflow-x-hidden">
                        {children}
                    </div>
                </>
            )}
        </main>
    )
}