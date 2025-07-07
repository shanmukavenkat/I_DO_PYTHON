import { JSXElementConstructor, Key, ReactElement, ReactNode, useState } from "react"
import { AnimatePresence, motion } from "framer-motion"

import useDetectBrowser from "../hooks/use-detect-browser"
import useScreenSize from "../hooks/use-screen-size"
import GooeySvgFilter from "@/fancy/components/filter/gooey-svg-filter"

const TAB_CONTENT = [
  {
    title: "AI-Driven Health Assistant",
    content: (
      <iframe
       src="https://asnvs-health.hf.space"
	frameBorder="0"
        className="w-full h-full min-h-[400px] overflow-scroll"
      ></iframe>
    ),
  },
  {
    title: "LungDisease Detection",
    content: (
        <iframe
         src="https://asnvs-lungdisease.hf.space"
	        frameBorder="0"
          className="w-full h-full min-h-[400px] overflow-scroll"
        ></iframe>
      ),
  },
  {
    title: "Symptoms to Disease Prediction",
    content: (
        <iframe
        src="https://asnvs-symptomsdiseasepredction.hf.space"
          frameBorder="0"
          className="w-full h-full min-h-[500px]"
        ></iframe>
      ),
  }
]

export default function GooeyDemo() {
  const [activeTab, setActiveTab] = useState(0)
  const [isGooeyEnabled] = useState(true)
  const screenSize = useScreenSize()
  const browserName = useDetectBrowser()
  const isSafari = browserName === "Safari"

  return (
    <div className="relative w-dvw h-dvh flex justify-center p-8 font-calendas md:text-base text-xs sm:text-sm bg-white dark:bg-black">
      <GooeySvgFilter
        id="gooey-filter"
        strength={screenSize.lessThan("md") ? 8 : 15}
      />

      <div className="w-11/12 md:w-4/5 relative mt-24">
        <div
          className="absolute inset-0"
          style={{ filter: isGooeyEnabled ? "url(#gooey-filter)" : "none" }}
        >
          <div className="flex w-full ">
            {TAB_CONTENT.map((_, index) => (
              <div key={index} className="relative flex-1 h-full md:h-12">
                {activeTab === index && (
                  <motion.div
                    layoutId="active-tab"
                    className="absolute inset-0 bg-[#efefef]"
                    transition={{
                      type: "spring",
                      bounce: 0.0,
                      duration: isSafari ? 0 : 0.4,
                    }}
                  />
                )}
              </div>
            ))}
          </div>
          {/* Content panel */}
          <div className="w-full h-full bg-[#efefef] overflow-hidden text-muted-foreground">
            <AnimatePresence mode="popLayout">
              <motion.div
                key={activeTab}
                initial={{ opacity: 0, y: 50, filter: "blur(10px)" }}
                animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                exit={{ opacity: 0, y: -50, filter: "blur(10px)" }}
                transition={{ duration: 0.2, ease: "easeOut" }}
                className="p-8 md:p-12 h-full "
              >
                {activeTab === 0 ? (
                  TAB_CONTENT[0].content
                ) : (
                  <ul>
                    {Array.isArray(TAB_CONTENT[activeTab].content) ? (
                      TAB_CONTENT[activeTab].content.map((content: ReactNode, index: number) => (
                        <li
                          key={index}
                          className="border-b border-muted-foreground/50 pt-2 pb-1  text-black"
                        >
                          {content}
                        </li>
                      ))
                    ) : (
                      TAB_CONTENT[activeTab].content
                    )}
                  </ul>
                )}
              </motion.div>
            </AnimatePresence>
          </div>
        </div>

        {/* Interactive text overlay, no filter */}
        <div className="relative flex w-full ">
          {TAB_CONTENT.map((tab, index) => (
            <button
              key={index}
              onClick={() => setActiveTab(index)}
              className="flex-1 h-8 md:h-12"
            >
              <span
                className={`
                w-full h-full flex items-center justify-center
                ${activeTab === index ? "text-black" : "text-muted-foreground"}
              `}
              >
                {tab.title}
              </span>
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
