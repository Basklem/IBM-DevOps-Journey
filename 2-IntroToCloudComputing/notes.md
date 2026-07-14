# Introduction to Cloud Computing — Notes

## Key Takeaways
- Cloud Computing Basics: Cloud provides on-demand access to computing resources with essential features like scalability, resource pooling, and measured service.
- Service Models: Understand IaaS (Infrastructure as a Service), PaaS (Platform as a Service), and SaaS (Software as a Service) as different ways cloud services are delivered.
- Deployment Models: Public, Private, and Hybrid clouds offer different levels of control, security, and flexibility.
- Cloud Components: Key elements include data centers, availability zones, virtual machines, containers, and storage options like object storage.
- Emerging Trends: Hybrid and multicloud strategies, microservices, serverless computing, cloud-native applications, DevOps, and application modernization are shaping cloud use.
- Cloud Providers: Major platforms include AWS, Microsoft Azure, Google Cloud, IBM Cloud, and Alibaba Cloud, each with unique services.
- Security and Monitoring: Cloud security practices and monitoring are critical for protecting data and ensuring performance.
- Career Opportunities: Cloud computing opens roles such as cloud engineer, DevOps engineer, cybersecurity analyst, and more.
- Hands-on Practice: Deploying applications using serverless architecture and other labs reinforce practical skills.

---
  
## Notes
- Cloud computing offers more flexibility and scalability than hosting on a local server. Why choose cloud vs. local server: latest business trends, extra bandwidth/faster internet speed, flexibility and scalability, availability, efficient marketing.
- NIST defines cloud computing as a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources (networks, servers, storage, applications, services). This includes 5 essential characteristics, 4 deployment models, and 3 service models.
- 5 Essential Characteristics:
  - On-demand self-service: access cloud resources whenever required, available 24/7 except during outages/security breaches (like a 24 hour ATM).
  - Broad network access: resources accessed through the network from anywhere, on any device with internet. Public cloud services require internet access; private cloud may have internet as well.
  - Resource pooling: computing resources serve multiple customers and are dynamically assigned/reassigned, saving on cost through a shared model.
  - Rapid elasticity: resources increase or decrease based on demand — vertical or horizontal scaling, adjusted to the number of users.
  - Measured service: pay for what you use or reserve, like a utility billing model (e.g., monthly electric charges). Not applicable to email services, social media, or trial-based services.
- Cloud computing dates back to the 1950s, when large-scale mainframes with high-volume processing power became available.
- Key drivers for moving to the cloud: agility, flexibility, and competitiveness — provided the move doesn't create business disruption or issues with security, compliance, and performance.
- IoT (Internet of Things) is a giant network of connected things and people that has changed how we live — from driving, to purchases, to monitoring personal health and home energy use.
- Blockchain is a secure, distributed, open technology that speeds up processes, lowers costs, and builds transparency/traceability in transactional applications. It's a secure, immutable network where members only view the transactions relevant to them.
- 3 Service Models (pyramid, bottom to top): IaaS (Infrastructure) -> PaaS (Platform) -> SaaS (Application/Software). Moving down the pyramid increases complexity; moving up increases ease of use.
  - IaaS: a set of computer, networking, and storage resources virtualized by a vendor so a user can access and use them however they want. Usually managed by a SysAdmin/IT admin. Key components: physical data centers (physical machines), compute (compute, memory, storage), network (virtualization/APIs), storage (object, file, block — object storage most common). Analogy: leasing a car.
  - PaaS: provides customers a complete platform to develop, deploy, manage, and run applications created by them or acquired from a third party. Takes advantage of IaaS resources without having to manage them yourself — usually used by devs. Analogy: renting a car.
  - SaaS: software you don't have to install or manually update. Analogy: taking a taxi.
- 4 Deployment Models indicate where the infrastructure resides, who owns/manages it, and how cloud resources/services are made available to users: Public, Private, Community, Hybrid.
  - Public Cloud: services accessible from anywhere, on any device, with internet access — mandatory for public cloud services.
  - Private Cloud (per NIST): cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers, such as business units within the organization.
  - Hybrid Cloud: connects an organization's on-premise private cloud and third-party public cloud into a single, flexible infrastructure for running applications/workloads. Complex and challenging to deploy and maintain. Example: leveraging public cloud instances temporarily, then returning to private cloud once demand is met — known as cloud bursting. Benefits: flexibility, workloads move freely, leverages both public and private clouds.
- The three tenets of hybrid cloud: interoperability, scalability, and portability.
- Types of Hybrid Clouds:
  - Hybrid mono cloud: a hybrid cloud with one cloud provider.
  - Hybrid multi-cloud: an open standards-based stack that can be deployed on any public cloud infrastructure.
- Cloud native applications are applications developed from the outset to work only in the cloud environment, or existing apps that have been refactored/reconfigured with cloud native principles.
- Cloud native development principles (whether creating a new app or modernizing an existing one):
  - Follow the microservices architectural approach by breaking applications down into single-function microservices.
  - Rely on containers for maximum flexibility, scalability, and portability.
  - Adopt Agile methods that speed the creation/improvement process through quick, iterative updates based on user feedback.
- To gain maximum benefit from interconnected cloud technologies, enterprises require the best cloud security procedures and technology. It's difficult to keep track of who is accessing your data and which cloud service they're using outside your organization.
- Considerations for each cloud service model: lack of visibility in a public cloud environment, multitenancy in a public cloud environment, access management and shadow IT, misconfiguration of assets.
- Threats and Risks in cloud computing:
  - Insider threats: caused by current/former employees, business partners, contractors, or anyone with past access to systems/networks — invisible to external security systems.
  - DDoS (Distributed Denial-of-Service): works through Simple Network Management Protocol (SNMP).
  - Data breach: due to a leak in cloud security measures.
- A shared responsibility model is a cloud security framework where the organization hands off certain IT security responsibilities to the cloud provider — each party is accountable for different aspects of security, depending on the service model:
  - IaaS: provider secures the physical infrastructure at their data centers; users are responsible for the security of software.
  - PaaS: provider secures the platform (OS, user subscriptions, login credentials); users are responsible for the security of any code, data, or other content produced on the platform.
  - SaaS: provider is responsible for almost every aspect of security (underlying infrastructure, service application, data the application produces); users still have some responsibilities, such as protecting login credentials.
- NIST has a list of best practices/principles for a secure and sustainable cloud computing framework — NIST's five pillars of a cybersecurity framework: Identify, Protect, Detect, Respond, Recover.
- Cloud Security Posture Management (CSPM) is an emerging technology that supports the cybersecurity framework. CSPM addresses: misconfigurations, IAM (Identity and Access Management), regulatory compliance management, traffic monitoring, threat response, risk mitigation, digital asset management.
- Unauthorized access through misuse of employee credentials and improper access controls is the single biggest perceived vulnerability to cloud security, followed by insecure interfaces and APIs, and data loss/leakage.
- Given concerns around data security and privacy — especially in public cloud environments — encryption plays a key role and is often referred to as the last line of defense in a layered security model.
