from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Test questions 
questions = {
    "Cloud Readiness": [ 
        {"question": "Does your organization have clear cloud adoption goals and timelines?", "id": "q1"},
        {"question": "Is cloud migration aligned with your long-term business objectives?", "id": "q2"},
        {"question": "Does the executive team actively support and prioritize cloud initiatives?", "id": "q3"},
        {"question": "Is there a dedicated cloud strategy team or cloud center of excellence (CoE)", "id": "q4"},
        {"question": "Are cross-functional teams (DevOps, Security, Networking) aligned for cloud migration?", "id": "q5"},
        {"question": "Does your technical staff have cloud certifications or experience with cloud platforms (AWS, Azure, GCP)?", "id": "q6"},
        {"question": "Is there a formal cloud training program or partnership with cloud vendors?", "id": "q7"},
        {"question": "Are teams trained in cloud-native architectures (microservices, serverless, etc.)?", "id": "q8"},
        {"question": "Is your on-prem infrastructure modernized or suitable for hybrid cloud solutions?", "id": "q9"},
        {"question": "Do you currently use virtualization and containerization technologies (VMware, Docker, Kubernetes)?", "id": "q10"},
        {"question": "Are there already existing integrations with public/private cloud providers?", "id": "q11"},
        {"question": "How adaptable is your organization to changes in technology and workflows?", "id": "q12"},
        {"question": "Is cloud seen as a strategic business enabler rather than a cost-saving tool?", "id": "q13"},
        {"question": "Do you have a clear cloud migration roadmap and defined success metrics?", "id": "q14"},
        {"question": "Has your organization evaluated the risks involved in cloud migration?", "id": "q15"},
        {"question": "Are contingency plans in place for critical applications during migration?", "id": "q16"},
        {"question": "Is there an assessment of vendor lock-in or potential service disruptions?", "id": "q17"},
    ],
    "Workload Suitability": [
        {"question": "Have you identified and documented all workloads currently running on-premises?", "id": "q18"},
        {"question": "Are critical applications clearly distinguished from less critical ones?", "id": "q19"},
        {"question": "Is there a categorization of workloads based on technical requirements, such as compute, storage, and network needs?", "id": "q20"},
        {"question": "Do your applications rely on specific hardware or software configurations that may not be easily replicated in the cloud?", "id": "q21"},
        {"question": "Have you identified any dependencies between applications that could complicate migration?", "id": "q22"},
        {"question": "Do any of your workloads have unpredictable scaling needs that would benefit from cloud elasticity?", "id": "q23"},
        {"question": "Are your workloads sensitive to latency, and have you assessed how cloud data center locations impact performance?", "id": "q24"},
        {"question": "Can your workloads handle potential performance variations inherent in shared cloud environments?", "id": "q25"},
        {"question": "Are your applications monolithic or already modular (e.g., microservices, serverless)?", "id": "q26"},
        {"question": "Are your applications built with modern frameworks that are cloud-native or cloud-compatible?", "id": "q27"},
        {"question": "How easy would it be to refactor or rearchitect applications to leverage cloud benefits?", "id": "q29"},
        {"question": "Is there a data migration strategy in place, including data volume assessments and potential downtime impacts?", "id": "q30"},
        {"question": "Are there concerns about data sovereignty, privacy, or compliance that affect where and how data can be stored?", "id": "q31"},
        {"question": "Do you use databases or data formats that are natively supported by cloud providers?", "id": "q32"},
        {"question": "Are there regulatory requirements or compliance standards (e.g., GDPR, HIPAA) that dictate how workloads can be migrated?", "id": "q33"},
        {"question": "Have you assessed the security implications of moving workloads to the cloud, including encryption and access controls?", "id": "q34"},
        {"question": "Can the existing security controls be extended or adapted to cloud environments?", "id": "q35"},
        {"question": "Have you evaluated the cost of running workloads in the cloud versus on-prem, including potential hidden costs (e.g., data egress fees)?", "id": "q36"},
        {"question": "Are there existing software licenses that could pose restrictions or additional costs when migrating to the cloud?", "id": "q37"},
        {"question": "Have you identified workloads that would benefit from cloud cost models like pay-as-you-go or reserved instances?", "id": "q38"},
    ],
    "Security & Compliance": [
        {"question": "Is there a defined security strategy that includes cloud environments?", "id": "q39"},
        {"question": "Are there clear roles and responsibilities for cloud security within your organization?", "id": "q40"},
        {"question": "Does your organization use centralized IAM solutions compatible with cloud platforms (e.g., AWS IAM)?", "id": "q41"},
        {"question": "Are multi-factor authentication (MFA) and least-privilege access enforced for cloud resources?", "id": "q42"},
        {"question": "Is there a policy for onboarding, managing, and offboarding user access to cloud resources?", "id": "q43"},
        {"question": "Are data encryption policies (at rest and in transit) established and compatible with cloud provider offerings?", "id": "q44"},
        {"question": "Do you have security monitoring solutions that can extend to or integrate with cloud services (e.g., SIEM, cloud-native monitoring tools)?", "id": "q45"},
        {"question": "Is there an incident response plan that includes cloud-specific scenarios and cloud service provider (CSP) roles?", "id": "q46"},
        {"question": "Are there established processes for logging, alerting, and auditing cloud activities?", "id": "q47"},
        {"question": "Do you maintain documentation and evidence of compliance readiness that includes cloud service providers?", "id": "q48"},
        {"question": "Are network security controls (e.g., firewalls, VPNs, WAFs) in place and adaptable to cloud networks?", "id": "q49"},
        {"question": "Have you assessed how current network segmentation and zero-trust architectures will translate to the cloud?", "id": "q50"},
        {"question": "Are there processes for securing API endpoints and ensuring secure communications between cloud services?", "id": "q51"},
        {"question": "Do you utilize cloud-native security tools (e.g., AWS Inspector) for vulnerability management?", "id": "q52"},
        {"question": "Do you have a process for assessing and managing security risks associated with cloud vendors?", "id": "q53"},
        {"question": "Are service-level agreements (SLAs) and shared responsibility models clearly understood and documented?", "id": "q54"},
        {"question": "Is there a continuous evaluation of third-party tools and integrations for security vulnerabilities?", "id": "q55"},
    ],
    "Cost & Budget": [
        {"question": "Has your organization developed a clear financial strategy for cloud migration, including expected cost savings and ROI?", "id": "q56"},
        {"question": "Do you have a documented budget specifically for cloud migration and ongoing cloud operations?", "id": "q57"},
        {"question": "Have you conducted a Total Cost of Ownership (TCO) analysis comparing on-premises vs. cloud costs?", "id": "q58"},
        {"question": "Are cloud cost estimation tools (e.g., AWS Pricing Calculator) being used to forecast expenses?", "id": "q59"},
        {"question": "Are cloud-native cost management tools (e.g., AWS Cost Explorer) integrated into your financial monitoring processes?", "id": "q60"},
        {"question": "Is there a standardized dashboard or reporting mechanism for tracking cloud costs across departments?", "id": "q61"},
        {"question": "Are cloud expenses broken down by department, project, or team to ensure accurate cost allocation?", "id": "q62"},
        {"question": "Do you have tagging and labeling policies for cloud resources to facilitate detailed cost tracking?", "id": "q63"},
        {"question": "Have you identified opportunities for cost savings, such as rightsizing instances, reserved instances, or spot instances?", "id": "q64"},
        {"question": "Do you leverage cloud provider discounts, savings plans, or custom pricing agreements?", "id": "q65"},
        {"question": "Are there policies in place for approving cloud expenses and ensuring that spending stays within budget limits?", "id": "q66"},
        {"question": "Is there a cloud financial governance framework to monitor and control costs in real-time?", "id": "q67"},
        {"question": "Have you evaluated existing software licenses for compatibility with cloud migration (e.g., bring-your-own-license)?", "id": "q68"},
        {"question": "Are there ongoing assessments of subscription models (pay-as-you-go vs. reserved capacity) to optimize costs?", "id": "q69"},
        {"question": "Are you aware of potential licensing pitfalls that could lead to unexpected expenses in the cloud?", "id": "q70"},
        {"question": "Are there ongoing efforts to educate teams on cloud cost management practices and financial accountability?", "id": "q71"},
        {"question": "Do you have FinOps metrics in place (e.g., cost per workload, cost per user) to measure cloud financial performance?", "id": "q72"},
    ],
    "Operations & DevOps": [
        {"question": "Are development and operations teams integrated, promoting a collaborative DevOps culture?", "id": "q73"},
        {"question": "Do you have cross-functional teams responsible for both development and ongoing support of applications in the cloud?", "id": "q74"},
        {"question": "Are Continuous Integration and Continuous Deployment (CI/CD) pipelines implemented and used consistently?", "id": "q75"},
        {"question": "Do you use automation tools (e.g., Jenkins, GitLab CI/CD, AWS CodePipeline) for building, testing, and deploying applications?", "id": "q76"},
        {"question": "Are infrastructure-as-code (IaC) tools (e.g., Terraform, AWS CloudFormation, Ansible) used to automate cloud resource provisioning?", "id": "q77"},
        {"question": "Do you have monitoring and logging solutions (e.g., Prometheus, Grafana) in place to track cloud application performance?", "id": "q78"},
        {"question": "Are cloud-native monitoring tools (e.g., AWS CloudWatch) integrated with your existing operations?", "id": "q79"},
        {"question": "Is there an established incident management process that includes cloud-specific considerations?", "id": "q80"},
        {"question": "Are your applications designed to leverage cloud auto-scaling capabilities for varying workloads?", "id": "q81"},
        {"question": "Do you use cloud-native services (e.g., load balancers, managed databases) to enhance application availability and reliability?", "id": "q82"},
        {"question": "Is there a focus on building and maintaining high-availability (HA) and disaster recovery (DR) plans for critical cloud applications?", "id": "q83"},
        {"question": "Are resource allocation and utilization regularly reviewed to ensure optimal performance and cost efficiency?", "id": "q84"},
        {"question": "Are configuration management tools (e.g., Puppet, Chef, SaltStack) used to maintain consistent environments across cloud and on-premises?", "id": "q85"},
        {"question": "Are compliance checks automated as part of your deployment pipelines to ensure that all cloud resources meet security and operational policies?", "id": "q86"},
        {"question": "Is there a process for collecting feedback on cloud operations to drive continuous improvements?", "id": "q87"},
        {"question": "Are teams encouraged to experiment and adopt new tools or practices that enhance cloud efficiency?", "id": "q88"},
        {"question": "Do you regularly review metrics and KPIs to identify areas for process improvements?", "id": "q89"},
        {"question": "Do you have policies for maintaining configuration drift and ensuring environments remain compliant with standards?", "id": "q90"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # Calculation of the total score
        scores = {key: int(value) for key, value in request.form.items()}
        total_score = sum(scores.values())
        max_score = len(scores) * 5  # Each question has a max score of 5
        percentage = (total_score / max_score) * 100

        # Recommended path based on the total score 
        if percentage >= 90:
            explanation = """
            Excellent! Your organization is very well-prepared for cloud migration. 
            You have strong technical and operational readiness, with most key areas well-covered. 
            You can confidently proceed with your migration strategy, focusing on execution and optimization.
            """
        elif percentage >= 75:
            explanation = """
            Great work! Your organization is quite ready for cloud migration, with solid foundations in place. 
            There may still be a few areas that need refinement, such as cost management or security practices. 
            Addressing these will ensure a smoother migration process.
            """
        elif percentage >= 60:
            explanation = """
            Good progress! Your organization has a moderate level of readiness. 
            While you've made strides in certain areas, other aspects such as workload suitability or team expertise 
            could benefit from additional attention. Consider refining your cloud strategy and preparing for challenges.
            """
        elif percentage >= 40:
            explanation = """
            Some readiness detected, but there are clear gaps. Your organization may struggle with certain aspects 
            of cloud migration, such as security, compliance, or workload suitability. 
            Prioritize these areas before moving forward with migration to minimize risks.
            """
        elif percentage >= 20:
            explanation = """
            Limited readiness. While your organization has made some initial efforts, significant improvements are required 
            in areas such as infrastructure, cloud knowledge, and security practices. 
            A detailed cloud migration plan is essential, and outside expertise might help you identify and address gaps.
            """
        else:
            explanation = """
            Not ready for cloud migration. There are critical gaps in your organization’s cloud readiness, 
            and moving forward without addressing them could lead to substantial risks. 
            Consider consulting cloud experts to help you build a structured plan and work towards cloud readiness in stages.
            """

        return render_template('test.html', questions=questions, scores=scores, total_score=total_score, explanation=explanation)
    
    return render_template('test.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
