import { Routes } from "@angular/router";

import { AssemblyGuidanceComponent } from "./pages/assembly-guidance.component";
import { ChangeFeedbackComponent } from "./pages/change-feedback.component";
import { DashboardComponent } from "./pages/dashboard.component";
import { DesignImpactComponent } from "./pages/design-impact.component";
import { IssueAtlasComponent } from "./pages/issue-atlas.component";
import { MechanicSignalHubComponent } from "./pages/mechanic-signal-hub.component";
import { SupplierIntegrityComponent } from "./pages/supplier-integrity.component";

export const routes: Routes = [
  { path: "", component: DashboardComponent },
  { path: "issue-atlas", component: IssueAtlasComponent },
  { path: "mechanic-signal-hub", component: MechanicSignalHubComponent },
  { path: "design-impact", component: DesignImpactComponent },
  { path: "supplier-integrity", component: SupplierIntegrityComponent },
  { path: "assembly-guidance", component: AssemblyGuidanceComponent },
  { path: "change-feedback", component: ChangeFeedbackComponent },
];
