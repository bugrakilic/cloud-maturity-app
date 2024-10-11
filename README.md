# Cloud Maturity App

The cloud maturity test aims to raise awareness for businesses interested in migrating their on-premises to the cloud platforms. 

The test includes below categories. User should select a readiness level for each question. The test evaluates the average score based on the answers, then recommends a path to the user. 

This is an open-source project. Please consider contributing. Any feedback is welcome. 

## Cloud Maturity Test Questions: 

#### Cloud Readiness:
- Does your organization have clear cloud adoption goals and timelines?
- Is cloud migration aligned with your long-term business objectives?
- Does the executive team actively support and prioritize cloud initiatives?
- Is there a dedicated cloud strategy team or cloud center of excellence (CoE)
- Are cross-functional teams (DevOps, Security, Networking) aligned for cloud migration?
- Does your technical staff have cloud certifications or experience with cloud platforms (AWS, Azure, GCP)?
- Is there a formal cloud training program or partnership with cloud vendors?
- Are teams trained in cloud-native architectures (microservices, serverless, etc.)?
- Is your on-prem infrastructure modernized or suitable for hybrid cloud solutions?
- Do you currently use virtualization and containerization technologies (VMware, Docker, Kubernetes)?
- Are there already existing integrations with public/private cloud providers?
- How adaptable is your organization to changes in technology and workflows?
- Is cloud seen as a strategic business enabler rather than a cost-saving tool?
- Do you have a clear cloud migration roadmap and defined success metrics?
- Has your organization evaluated the risks involved in cloud migration?
- Are contingency plans in place for critical applications during migration?
- Is there an assessment of vendor lock-in or potential service disruptions?

#### Workload Suitability: 
- Have you identified and documented all workloads currently running on-premises?
- Are critical applications clearly distinguished from less critical ones?
- Is there a categorization of workloads based on technical requirements, such as compute, storage, and network needs?
- Do your applications rely on specific hardware or software configurations that may not be easily replicated in the cloud?
- Have you identified any dependencies between applications that could complicate migration?
- Do any of your workloads have unpredictable scaling needs that would benefit from cloud elasticity?
- Are your workloads sensitive to latency, and have you assessed how cloud data center locations impact performance?
- Can your workloads handle potential performance variations inherent in shared cloud environments?
- Are your applications monolithic or already modular (e.g., microservices, serverless)?
- Are your applications built with modern frameworks that are cloud-native or cloud-compatible?
- How easy would it be to refactor or rearchitect applications to leverage cloud benefits?
- Is there a data migration strategy in place, including data volume assessments and potential downtime impacts?
- Are there concerns about data sovereignty, privacy, or compliance that affect where and how data can be stored?
- Do you use databases or data formats that are natively supported by cloud providers?
- Are there regulatory requirements or compliance standards (e.g., GDPR, HIPAA) that dictate how workloads can be migrated?
- Have you assessed the security implications of moving workloads to the cloud, including encryption and access controls?
- Can the existing security controls be extended or adapted to cloud environments?
- Have you evaluated the cost of running workloads in the cloud versus on-prem, including potential hidden costs (e.g., data egress fees)?
- Are there existing software licenses that could pose restrictions or additional costs when migrating to the cloud?
- Have you identified workloads that would benefit from cloud cost models like pay-as-you-go or reserved instances?

#### Security & Compliance: 
- Is there a defined security strategy that includes cloud environments?
- Are there clear roles and responsibilities for cloud security within your organization?
- Does your organization use centralized IAM solutions compatible with cloud platforms (e.g., AWS IAM)?
- Are multi-factor authentication (MFA) and least-privilege access enforced for cloud resources?
- Is there a policy for onboarding, managing, and offboarding user access to cloud resources?
- Are data encryption policies (at rest and in transit) established and compatible with cloud provider offerings?
- Do you have security monitoring solutions that can extend to or integrate with cloud services (e.g., SIEM, cloud-native monitoring tools)?
- Is there an incident response plan that includes cloud-specific scenarios and cloud service provider (CSP) roles?
- Are there established processes for logging, alerting, and auditing cloud activities?
- Do you maintain documentation and evidence of compliance readiness that includes cloud service providers?
- Are network security controls (e.g., firewalls, VPNs, WAFs) in place and adaptable to cloud networks?
- Have you assessed how current network segmentation and zero-trust architectures will translate to the cloud?
- Are there processes for securing API endpoints and ensuring secure communications between cloud services?
- Do you utilize cloud-native security tools (e.g., AWS Inspector) for vulnerability management?
- Do you have a process for assessing and managing security risks associated with cloud vendors?
- Are service-level agreements (SLAs) and shared responsibility models clearly understood and documented?
- Is there a continuous evaluation of third-party tools and integrations for security vulnerabilities?

#### Cost & Budget: 
- Has your organization developed a clear financial strategy for cloud migration, including expected cost savings and ROI?
- Do you have a documented budget specifically for cloud migration and ongoing cloud operations?
- Have you conducted a Total Cost of Ownership (TCO) analysis comparing on-premises vs. cloud costs?
- Are cloud cost estimation tools (e.g., AWS Pricing Calculator) being used to forecast expenses?
- Are cloud-native cost management tools (e.g., AWS Cost Explorer) integrated into your financial monitoring processes?
- Is there a standardized dashboard or reporting mechanism for tracking cloud costs across departments?
- Are cloud expenses broken down by department, project, or team to ensure accurate cost allocation?
- Do you have tagging and labeling policies for cloud resources to facilitate detailed cost tracking?
- Have you identified opportunities for cost savings, such as rightsizing instances, reserved instances, or spot instances?
- Do you leverage cloud provider discounts, savings plans, or custom pricing agreements?
- Are there policies in place for approving cloud expenses and ensuring that spending stays within budget limits?
- Is there a cloud financial governance framework to monitor and control costs in real-time?
- Have you evaluated existing software licenses for compatibility with cloud migration (e.g., bring-your-own-license)?
- Are there ongoing assessments of subscription models (pay-as-you-go vs. reserved capacity) to optimize costs?
- Are you aware of potential licensing pitfalls that could lead to unexpected expenses in the cloud?
- Are there ongoing efforts to educate teams on cloud cost management practices and financial accountability?
- Do you have FinOps metrics in place (e.g., cost per workload, cost per user) to measure cloud financial performance?

#### Operations & DevOps: 
- Are development and operations teams integrated, promoting a collaborative DevOps culture?
- Do you have cross-functional teams responsible for both development and ongoing support of applications in the cloud?
- Are Continuous Integration and Continuous Deployment (CI/CD) pipelines implemented and used consistently?
- Do you use automation tools (e.g., Jenkins, GitLab CI/CD, AWS CodePipeline) for building, testing, and deploying applications?
- Are infrastructure-as-code (IaC) tools (e.g., Terraform, AWS CloudFormation, Ansible) used to automate cloud resource provisioning?
- Do you have monitoring and logging solutions (e.g., Prometheus, Grafana) in place to track cloud application performance?
- Are cloud-native monitoring tools (e.g., AWS CloudWatch) integrated with your existing operations?
- Is there an established incident management process that includes cloud-specific considerations?
- Are your applications designed to leverage cloud auto-scaling capabilities for varying workloads?
- Do you use cloud-native services (e.g., load balancers, managed databases) to enhance application availability and reliability?
- Is there a focus on building and maintaining high-availability (HA) and disaster recovery (DR) plans for critical cloud applications?
- Are resource allocation and utilization regularly reviewed to ensure optimal performance and cost efficiency?
- Are configuration management tools (e.g., Puppet, Chef, SaltStack) used to maintain consistent environments across cloud and on-premises?
- Are compliance checks automated as part of your deployment pipelines to ensure that all cloud resources meet security and operational policies?
- Is there a process for collecting feedback on cloud operations to drive continuous improvements?
- Are teams encouraged to experiment and adopt new tools or practices that enhance cloud efficiency?
- Do you regularly review metrics and KPIs to identify areas for process improvements?
- Do you have policies for maintaining configuration drift and ensuring environments remain compliant with standards?