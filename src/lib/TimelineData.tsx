import Image from "next/image"

export const TimelineData = [
    {
        title: "2020",
        content: (
            <div>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-8">
                    Learnt Python and worked on a few small projects to familiarize myself.
                </p>
                <div className="grid grid-cols-2 gap-4">
                    <Image
                        src="/timeline/2020_1.png"
                        alt="timeline 2020-1"
                        width={500}
                        height={500}
                        className="rounded-lg object-contain h-20 md:h-44 lg:h-60 w-fit shadow-lg"
                    />
                    <Image
                        src="/timeline/2020_2.png"
                        alt="timeline 2020-2"
                        width={500}
                        height={500}
                        className="rounded-lg object-contain h-20 md:h-44 lg:h-60 w-fit shadow-lg"
                    />
                    <Image
                        src="/timeline/2020_3.png"
                        alt="timeline 2020-3"
                        width={500}
                        height={500}
                        className="rounded-lg object-contain h-20 md:h-44 lg:h-60 w-fit shadow-lg"
                    />
                    {/* <Image
                        src=""
                        alt="startup template"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    /> */}
                </div>
            </div>
        ),
    },
    {
        title: "2021-2022",
        content: (
            <div>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-8">
                    At this point I felt confident enough to experiment with and learn other programming languages.
                </p>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-8">
                    I started to pick up on the syntax and semantics of languages like Swift, Java, Javascript, C#, Kotlin, etc.
                </p>
                <div className="grid grid-cols-2 gap-4">
                    <Image
                        src="/timeline/2021_1.png"
                        alt="timeline 2021-1"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2021_2.png"
                        alt="timeline 2021-2"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2021_3.png"
                        alt="timeline 2021-3"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2021_4.png"
                        alt="timeline 2021-4"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                </div>
            </div>
        ),
    },
    {
        title: "2023",
        content: (
            <div>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-4">
                    This is the year that I started to tinker with web development.
                </p>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-4">
                    I explored many frameworks and libraries such as Flutter, Django, Vue (as well as static HTML), but
                    ultimately settled on Next.js for its ease of use and flexibility.
                </p>
                <div className="grid grid-cols-2 gap-4">
                    <Image
                        src="/timeline/2023_1.png"
                        alt="timeline 2023-1"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2023_2.png"
                        alt="timeline 2023-2"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    {/* <Image
                        src="/timeline/2023_3.png"
                        alt="bento template"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    /> */}
                    <Image
                        src="https://github-readme-stats.vercel.app/api/wakatime?username=imapotatoes11&layout=compact&langs_count=8"
                        alt="timeline 2023-3"
                        width={500}
                        height={500}
                        className="rounded-lg object-contain w-fit shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                </div>
            </div>
        ),
    },
    {
        title: "2024",
        content: (
            <div>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-4">
                    Up until now, I&apos;ve been continuously familiarizing myself with not only Next.js, but also other languages, frameworks, libraries alike.
                </p>
                <p className="text-neutral-800 dark:text-neutral-200 text-md font-normal mb-4">
                    I also began to work on (and actually finish) my own projects, such as this website, to showcase my skills and knowledge.
                </p>
                <div className="grid grid-cols-2 gap-4">
                    <Image
                        src="/timeline/2024_1.png"
                        alt="timeline 2024-1"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2024_2.png"
                        alt="timeline 2024-2"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2024_3.png"
                        alt="timeline 2024-3"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                    <Image
                        src="/timeline/2024_4.png"
                        alt="timeline 2024-4"
                        width={500}
                        height={500}
                        className="rounded-lg object-cover h-20 md:h-44 lg:h-60 w-full shadow-[0_0_24px_rgba(34,_42,_53,_0.06),_0_1px_1px_rgba(0,_0,_0,_0.05),_0_0_0_1px_rgba(34,_42,_53,_0.04),_0_0_4px_rgba(34,_42,_53,_0.08),_0_16px_68px_rgba(47,_48,_55,_0.05),_0_1px_0_rgba(255,_255,_255,_0.1)_inset]"
                    />
                </div>
            </div>
        ),
    }
];