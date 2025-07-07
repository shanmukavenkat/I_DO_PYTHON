import Header from "@/components/Header";
import Displayscomponent from '@/components/Displayscomponent'
import UserDetails from "./UserDetails";
const Dashboard = () => {
    return (
        <div>
            <Header/>
            <UserDetails/>
            
           <div className="m-3">
           <Displayscomponent/>
           </div>
        </div>
    )
}
export default Dashboard