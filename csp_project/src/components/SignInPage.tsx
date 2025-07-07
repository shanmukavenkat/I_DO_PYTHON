import { SignInButton } from "@clerk/clerk-react";
import { Button } from "@/components/ui/button";
import { FaHeartbeat, FaLungs, FaStethoscope } from "react-icons/fa";
import { motion } from "framer-motion";

const HomePage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-indigo-800 to-purple-900 text-white flex flex-col items-center p-6 overflow-hidden">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: "easeOut" }}
        className="text-center mt-20 z-10"
      >
        <h1 className="text-5xl md:text-6xl font-extrabold flex items-center justify-center gap-4 tracking-tight">
          <FaHeartbeat className="text-red-400 animate-pulse" />
          AI-Driven Health Assistant
        </h1>
        <p className="text-lg md:text-xl mt-6 max-w-2xl mx-auto leading-relaxed opacity-90">
          Discover instant health insights with cutting-edge AI. Analyze symptoms, detect lung diseases, or receive personalized recommendations.
        </p>
        <Button
          variant="outline"
          className="mt-8 bg-transparent border-2 border-white text-white font-semibold py-3 px-8 rounded-full hover:bg-white hover:text-indigo-900 transition-all duration-300"
        >
          <SignInButton>Start Now</SignInButton>
        </Button>
      </motion.div>

      {/* Features Section */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 1 }}
        className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-5xl"
      >
        <FeatureCard
          icon={<FaStethoscope className="text-teal-300" />}
          title="AI Health Assistant"
          description="Input symptoms and receive AI-powered medicine suggestions instantly."
        />
        <FeatureCard
          icon={<FaLungs className="text-blue-300" />}
          title="Lung Disease Detection"
          description="Upload scans for AI-driven detection of potential lung conditions."
        />
        <FeatureCard
          icon={<FaHeartbeat className="text-red-300" />}
          title="Symptom Prediction"
          description="Get real-time disease predictions based on your symptoms."
        />
      </motion.div>

      {/* Background Decorative Element */}
      <div className="absolute inset-0 -z-10 opacity-20">
        <div className="w-full h-full bg-[radial-gradient(circle_at_center,#ffffff_1px,transparent_1px)] bg-[length:20px_20px]"></div>
      </div>
    </div>
  );
};

interface FeatureCardProps {
  icon: React.ReactNode;
  title: string;
  description: string;
}

const FeatureCard = ({ icon, title, description }: FeatureCardProps) => {
  return (
    <motion.div
      whileHover={{ scale: 1.05, y: -10 }}
      whileTap={{ scale: 0.95 }}
      className="p-6 bg-white bg-opacity-10 backdrop-blur-md rounded-xl shadow-lg text-center flex flex-col items-center border border-white border-opacity-20 transition-all duration-300 hover:bg-opacity-20"
    >
      <div className="text-5xl mb-4">{icon}</div>
      <h3 className="text-xl font-semibold tracking-wide">{title}</h3>
      <p className="text-sm mt-3 opacity-80 leading-relaxed">{description}</p>
    </motion.div>
  );
};

export default HomePage;