'use client';
import Navigator from '@/components/Navigator';
import { useEffect, useState } from 'react';
import { Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure } from "@nextui-org/react";

export default function Home() {
    const [isMobile, setIsMobile] = useState(false);
    const { isOpen, onOpen, onOpenChange } = useDisclosure();

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
        <main>
            <Navigator>
                <div className={`${isMobile ? 'h-[85vh]' : 'h-screen'} w-full flex flex-row justify-center align-center items-center`}>
                    Hi
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
                                    The site is currently incomplete. This only exists as a skeleton/scaffold for future development. Please check back later.
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
        </main>
    );
}