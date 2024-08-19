'use client';
import Navigator from '@/components/Navigator';
import { useEffect, useState } from 'react';
import { Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure, Select, SelectItem } from "@nextui-org/react";
// import { useDisclosure } from '@nextui-org/react';
import ConfigButton from '@/components/ConfigButton';
import { Meteors } from "@/components/magicui/meteors";
import GridPattern from "@/components/magicui/animated-grid-pattern";
import DotPattern from "@/components/magicui/dot-pattern";
import Particles from "@/components/magicui/particles";
import { BorderBeam } from '@/components/magicui/border-beam';
import { cn } from '@/lib/utils';

export default function Home() {
    const [isMobile, setIsMobile] = useState(false);
    const { isOpen, onOpen, onOpenChange } = useDisclosure();
    const [darkMode, setDarkMode] = useState(false);

    const possibleBgs = ["meteors", "grid", "dots", "particles"];
    const [selectedBg, setSelectedBg] = useState("meteors");

    // for settings modal
    const settings = useDisclosure();

    const scrollDownByOneViewHeight = () => {
        window.scrollBy({
            top: window.innerHeight,
            behavior: "smooth"
        });
    }

    useEffect(() => {
        const observer = new MutationObserver(() => {
            setDarkMode(document.documentElement.classList.contains('dark'));
        });

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['class'],
        });

        // Set initial state
        setDarkMode(document.documentElement.classList.contains('dark'));

        return () => {
            observer.disconnect();
        };
    }, []);

    useEffect(() => {
        setSelectedBg(localStorage.getItem('selectedBg') || "meteors");
    }, []);

    useEffect(() => {
        // save to localStorage whenever selectedBg changes
        localStorage.setItem('selectedBg', selectedBg);
    }, [selectedBg]);

    useEffect(() => {
        const userAgent = typeof window.navigator === 'undefined' ? '' : navigator.userAgent;
        const mobile = Boolean(
            userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i)
        );
        setIsMobile(mobile);
    }, []);

    useEffect(() => {
        onOpen();
    }, [])

    return (
        <main className="transition-all">
            <Navigator>
                {selectedBg === "meteors" && <Meteors number={20} />}
                {selectedBg === "grid" && <GridPattern className={cn(
                    "[mask-image:radial-gradient(500px_circle_at_center,white,transparent)]",
                    "inset-x-0 inset-y-[-30%] h-[200%] -skew-y-12 translate-y-[-20vh]",
                )} />}
                {selectedBg === "dots" && <DotPattern className={cn(
                    "[mask-image:radial-gradient(750px_circle_at_center,white,transparent)]",
                    // "inset-x-0 inset-y-[-30%] h-[200%] skew-y-12 translate-y-[-20vh]",
                )} />}
                {selectedBg === "particles" && <Particles quantity={100} ease={80} refresh className="absolute inset-0" color={darkMode ? '#dfdfdf' : '#212121'} size={2} />}
                <div className={`${isMobile ? 'h-[85vh]' : 'h-screen'} w-full flex flex-row justify-center align-center items-center`}>
                    <div className="transition-all flex flex-row justify-center items-center p-8 rounded-2xl backdrop-blur-sm">
                        <BorderBeam size={300} duration={12} delay={9} colorFrom={darkMode ? '#dfdfdf' : '#212121'} colorTo={darkMode ? '#212121' : '#dfdfdf'} />
                        <div className="flex flex-col gap-6">
                            <h1 className="text-6xl">
                                Hi,<br />I&apos;m
                                <span
                                    className="font-bold static-gradient-2"
                                    id="title-name"
                                > Kevin</span>
                                .
                            </h1>
                            <p>
                                Student / Programmer / Pianist / Vid<span
                                    className="hover:text-teal-500 cursor-pointer"
                                    onClick={() => window.location.href = 'https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fmy-furina-fanart-v0-mhazgiu328ac1.png%3Fauto%3Dwebp%26s%3Df951d1fdbdb917293031273cdc49453c14a4aa96'}
                                >e</span
                                >o Games Enjoyer
                            </p>
                            <div
                                className="group w-fit cursor-pointer"
                                onClick={() => scrollDownByOneViewHeight()}
                            >
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    strokeWidth="1.5"
                                    stroke="currentColor"
                                    className="transition-all size-6 group-hover:translate-y-2 cursor-pointer"
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        d="M19.5 13.5 12 21m0 0-7.5-7.5M12 21V3"
                                    />
                                </svg>
                            </div>
                        </div>
                        <div className="p-12"></div>
                    </div>
                </div>
                <div className={`${isMobile ? 'h-[95vh]' : 'h-screen'} w-full flex flex-row justify-center align-center items-center bg-base-200`}>
                    about
                </div>
                <div className={`${isMobile ? 'h-[95vh]' : 'h-screen'} w-full flex flex-row justify-center align-center items-center`}>
                    projects
                </div>
            </Navigator>
            <Modal isOpen={isOpen} onOpenChange={onOpenChange}>
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader className="flex flex-col gap-1">Modal Title</ModalHeader>
                            <ModalBody>
                                <p>
                                    The site is currently under active development. Please check back later.
                                </p>
                            </ModalBody>
                            <ModalFooter>
                                <Button color="primary" onPress={onClose}>
                                    Close
                                </Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
            <Modal isOpen={settings.isOpen} onClose={settings.onOpenChange}>
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader>Settings</ModalHeader>
                            <ModalBody>
                                <div className="flex flex-col gap-3">
                                    <div className="flex flex-row justify-between gap-4">
                                        <span>Dynamic Background</span>
                                        <Select
                                            value={selectedBg}
                                            onChange={(e) => setSelectedBg(e.target.value)}
                                            label="Select a background"
                                        >
                                            {possibleBgs.map(bg => <SelectItem key={bg} value={bg}>{bg}</SelectItem>)}
                                        </Select>
                                    </div>
                                </div>
                            </ModalBody>
                            <ModalFooter>
                                <Button onClick={settings.onOpenChange}>Close</Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
            <ConfigButton position="topright" onClick={settings.onOpen}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
            </ConfigButton>

        </main>
    );
}