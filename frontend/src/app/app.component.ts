import { NgFor } from "@angular/common";
import { Component } from "@angular/core";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [NgFor],
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
})
export class AppComponent {
  modules = [
    {
      title: "Issue Atlas",
      description: "Unified defect map across manufacturing, service, and suppliers.",
    },
    {
      title: "Mechanic Signal Hub",
      description: "AI summarization and trend detection from service notes.",
    },
    {
      title: "Design Impact Simulator",
      description: "Connect recurring issues to components and design decisions.",
    },
    {
      title: "Supplier Integrity Dashboard",
      description: "Risk scoring and anomaly detection for supplier quality.",
    },
    {
      title: "Assembly Guidance Generator",
      description: "Translate design intent into clear shop-floor steps.",
    },
    {
      title: "Change Feedback Loop",
      description: "Measure improvement after fixes roll out.",
    },
  ];
}
