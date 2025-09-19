import { Sidebar } from "@/components/layout/Sidebar";
import { MobileNav } from "@/components/layout/MobileNav";
import { DashboardCards } from "@/components/dashboard/DashboardCards";

const Index = () => {
  return (
    <div className="min-h-screen bg-gradient-background">
      {/* Mobile Navigation */}
      <MobileNav />
      
      <div className="flex">
        {/* Desktop Sidebar */}
        <Sidebar className="hidden lg:block" />
        
        {/* Main Content */}
        <main className="flex-1 lg:p-8 p-4 pb-20 lg:pb-8">
          <div className="max-w-7xl mx-auto">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-foreground mb-2">
                Welcome back, John! 👋
              </h1>
              <p className="text-muted-foreground">
                Here's an overview of your financial activity.
              </p>
            </div>
            
            <DashboardCards />
          </div>
        </main>
      </div>
    </div>
  );
};

export default Index;
