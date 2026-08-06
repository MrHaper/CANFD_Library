---
title: iCC 2020 论文 — CAN Signal Improvement and Designing 5-Mbps Networks(全文查阅)
description: 2020 年国际 CAN 大会(iCC 2020)论文全文:讲解 CAN Signal Improvement(CAN-SIC)技术如何突破 CAN FD 网络的速度极限、实现 5 Mbps 网络,含最坏情况分析、仿真建议、拓扑准则、采样点选择与线缆选择。
type: 全文查阅
organization: NXP Semiconductors
year: 2020
tags: [全文查阅, 论文]
source: https://www.can-newsletter.org/assets/files/Proceedings_2020_ICC.pdf
---

# CAN Signal Improvement and Designing 5-Mbps Networks(全文查阅)

> **论文**:iCC 2020(iCC — international CAN Conference),CAN in Automation
> **作者**:Tony Adamson, Axel Engelhard, Edmund Zhang(NXP Semiconductors)
> **原文 PDF**:[📄 下载原文 PDF](../../files/papers/2020_Adamson_CAN_signal_improvement_and_5Mbps_networks.pdf)
> **相关资料**:[资源条目页](../_entries/papers/2020-adamson-5mbps-networks.md)

---

CAN Signal Improvement technology can greatly simplify the creation of CAN FD networks at 2 Mbps and allow much larger topologies to be supported than with standard High Speed CAN (HS-CAN) transceivers. However, increasing interest is also appearing to use CAN Signal Improvement technology to enable 5 Mbps networks, further accelerating the achievable bandwidth with CAN FD. Traditional HS-CAN transceivers have been more or less limited to point-to-point networks at 5 Mbps, impractical for use in many applications. In this paper, the background to this limit is explained and guidelines are shared on creating robust 5 Mbps CAN FD networks based on our experiences of working with customers.

## Review: The fundamental speed limit of CAN FD communication

As reviewed in several previous papers [1], [2], [3], while it is possible to create examples of fast CAN FD networks operating on a laboratory bench, to create a robust network that is replicable millions of times requires a full worst-case analysis to guarantee network operation. [1] outlined a "Corrected Sample Point", or more generally, a "Safe Operating Area" for signals, based on worst-case asymmetry timings. This could be used as pass/fail criteria to check network simulation results against, to see if network signals remained inside the safe operating area across all combinations of signals between nodes on the network.

As this has been discussed at length in [1], only a brief recap is included here as way of review.

This analysis assumes all network nodes or electronic control units (ECUs) are implemented considering the recommendations described in the CiA 601-3 [4]. Without these recommendations being implemented, there are likely more fundamental problems possible, for which the techniques in this paper will not solve.

We take a worst-case bit pattern of 5 dominant bits followed by 1 recessive bit as the longest period between a synchronization point of the network until a sample point, and overlay the associated asymmetries to define the boundaries of the safe operating area and identifying the areas that must be avoided.

The example in Figure 1 considers a node receiving a remote sender's CAN FD transmission, operating at 2 Mbps. Table 1 identifies the different worst-case component asymmetries for the recessive bit (the most vulnerable to signal ringing), which are independent and thus cumulatively added together. The most relevant conclusion for CAN FD networks that are affected by signal ringing is that the signal must settle below the 0.5 V ahead of the earliest sample point, which is significantly earlier than the nominal sample point set in the CAN FD controller.

> Figure 1: Example of worst-case asymmetries in CAN FD network at 2 Mbps (for receiving node)

**Table 1: Components of timing asymmetry for recessive bit (receive node shown only)**

In [1], there is also an independent calculation for the sending node, reading back its own signal.

## Colliding worst cases and a new breakthrough

A major contributor to the total asymmetry calculation is the asymmetry of the physical layer transceiver. This asymmetry is constant and does not decrease when the bit rate increases, meaning it gets proportionally a much larger percentage of the bit time at higher bit rates. The earliest possible sample point in the final recessive bit moves relatively earlier; likewise, the latest possible sample point in the previous dominant bit moves relatively later. The point at which these two collide, visualized in simplified form in Figure 2, becomes the critical blocking point to achieving reliable faster CAN FD networks — without even considering topology effects like signal ringing; this applies even in well terminated, point-to-point networks.

> Figure 2: Simplified visualization of worst-case sample points colliding as bit rates increases.

Extending the above, we can visualize this effect across multiple bit rates by plotting the earliest sample point in the recessive bit alongside the latest sample point in the dominant bit. Figure 3 shows this plot, indicating the two worst-cases collide around 6 Mbps, defining the maximum achievable bit rate. As an aside, some HS-CAN transceivers already claim 8 Mbps operation in their datasheets; plugging their stated min/max values into this calculation shows these claims may not always be reliable when part of such a worst-case network analysis. User judgement is advised.

> Figure 3: Graph showing collision of worst-case sample points for ISO 11898-2:2016 compliant HS-CAN transceivers.

The breakthrough to overcome this speed limit is offered by CAN transceivers with Signal Improvement Capability (CAN-SIC) and defined in the CiA 601-4 specification [5]. The CiA 601-4 specifies a much tighter asymmetry for these devices: ±10 ns for the transmitter and -20…+15 ns for the receiver, gaining 60 ns compared to the values of the ISO 11898-2:2016. Plotting a similar graph with these worst-case asymmetries shows a clear improvement in the theoretical limit for CAN FD communication, moving far beyond 8 Mbps in a point-to-point network, when considering asymmetry alone.

> Figure 4: Graph showing extended bit rates possible with CiA 601-4 compliant CAN-SIC transceivers.

The margin available at 5 Mbps with CAN-SIC transceivers is still significant — slightly less than available with standard HS-CAN transceivers at 2 Mbps. Since this is time where no sampling will ever be made, the signal is free to be disturbed, so long as it returns below the 0.5 V level by the earliest recessive sample point; this can be referred to as the "Allowable Ringing Time". This is where the second breakthrough of CAN-SIC transceivers benefits network design: by reducing the signal ringing in the recessive bits and quickly bringing the signal below the 0.5 V receiver level.

By way of illustration, Figure 5 shows example simulations based on a real-world network, comparing A) 2 Mbps bit rate with a HS-CAN transceiver, B) 2 Mbps bit rate with a CAN-SIC transceiver, C) 5 Mbps bit rate with a HS-CAN transceiver, and D) 5 Mbps bit rate with a CAN-SIC transceiver. Highlighted in red is the boundary of the safe operating area for the signal. Note, these simulations show a more complex bit pattern, the rationale for which will be explained later in the paper.

> Figure 5: 4 example simulations of HS-CAN and CAN-SIC transceivers at 2 and 5 Mbps.

Example A) with a HS-CAN transceiver shows some ringing above the 0.5 V threshold still within the safe operating area, so this network would be fully reliable at 2 Mbps. Example B) shows the benefit of the CAN-SIC transceiver reducing the ringing peak to below the 0.5 V. Now comparing examples C) and D), the safe operating area for the HS-CAN transceiver becomes very narrow due to the asymmetry and any ringing above the 0.5 V limit prevents reliable operation of this network. By contrast in D), the CAN Signal Improvement transceiver both extends the safe operating area and brings the signal quickly below the 0.5 V threshold (the remaining peak is far below this threshold, so not relevant). This shows how both effects work together to make 5 Mbps CAN FD networks feasible with significant margin.

## Recommendations for 5-Mbps networks

Having demonstrated practical 5 Mbps CAN FD networks are feasible using CAN-SIC transceivers, some recommendations are provided in terms of network assessment strategies and 5 Mbps network design.

The first recommendation has already been covered in the introduction, namely using network simulations in combination with a worst-case assessment criterion for judging whether a network will be robust or not. Some additional points are worth mentioning in more detail, however.

### Defining the worst-case simulation

The starting point for making a worst-case assessment is there will always be spread in component specifications, which will be seen over millions of devices — and therefore the assessment should cater for this. Additionally, the most extreme operating conditions should be tested in the network simulation to be perfectly safe. This is normally considered as the worst-case simulation model option provided by transceiver simulation models as of today.

In reality, however, taking all worst-case timing specification conditions cumulatively, together with the worst-case simulation model option is not realistic. The combination of all transceiver specification parameters being at the same extreme edge, in combination with, for example, the highest VCC input level, is not possible even though the data sheet suggests it.

A data sheet takes each characteristic parameter as an individual possible number without saying which combination of all characteristics at a single moment in time is possible, while the simulation model drives all these parameters to the data sheet limits through the according simulation control parameter. Further, a transceiver's output driver stability over temperature is much more stable than the data sheet limits are predicting. The most relevant temperature related effect is the timing performance.

Our recommendation is therefore to use the typical simulation model option, together with the worst-case asymmetry assessment, which is already mapping reality, even when considering all temperature and potential aging effects. This view has been reviewed and supported by multiple customers and car makers.

The advantage of this approach is not purely to increase the achievable operating space of the network, although this is a desirable benefit. It has the added advantage that simulation results can be easily cross-checked with bench testing, since the simulation conditions used are the same and are already mapping closely with real-world behaviour. By optional variation of the VCC voltage in accordance with the used application regulator, the impact can likewise easily be observed in simulation and in bench testing.

Turning it around, this approach also allows bench test measurements to be assessed with the same safe operating area, to already provide a first indication if the network will operate reliably. This can simplify early pre-assessments on a network, giving early insights if a topology will operate robustly, while giving confidence cross-checking simulation results once they are available.

### Bit pattern choice for simulation

As highlighted in the example simulations, a more complex bit pattern is recommended for use in network simulations. This consists of one dominant bit and one recessive bit, followed by five dominant bits and one recessive bit, and then finally one dominant bit and one recessive bit.

The rationale to consider this more complex bit pattern is to consider the worst cases of communication, namely the shortest dominant bit combination followed by a recessive bit, as well as the longest dominant bit combination followed by a recessive bit. The longest dominant bit pattern allows the longest oscillator drift possible, maximizing the total asymmetry (as shown in Table 1); the shortest dominant bit pattern checks if any remaining ringing in the dominant bit might interfere with the next recessive bit.

Consequently, we advocate to use both combinations in the network simulation input stimuli, so that both scenarios can be checked in a single simulation.

### Use of warning areas around safe operating areas

It is recommended to use warning areas around the safe operating area boundary as opposed to a simple OK / Not OK judgement. The intention of this is to indicate early to network architects where in the network signals are getting close to the edge, which may expedite bench testing measurements to cross-check.

Based on experience, we recommend a 25 ns timing buffer around the safe operating area boundary, and a 0.05 V buffer on the vertical axis. The latter safe-guards in case a reflected peak comes very close to either the 0.5 V or 0.9 V threshold, but not high enough to trigger a fail. Without using a warning, this would just appear as just another pass in a large number of simulation results. Consider assessing n number of ECUs creates n² number of simulations results; navigating this large dataset efficiently and having flags of attention points is highly valuable.

The use of a warning flag can easily identify cases to cross-check via bench testing to determine if this is a concerning issue or not. For those that also wish to include extra margin for items like high powered EM noise injection, cable variation, VCC spread, etc. this also serves the secondary purpose of making a full pass even more reliable.

It should be noted, that a real receiver implementation has a very stable threshold voltage of about 0.7 V and the 0.5 V limit of data sheets is more a formal limit coming from the CAN ISO standard. As such, there is already a huge safety margin when taking 0.5 V as Pass/Fail criteria. The warning is only intended to make data analysis more efficient and not to add even more margin on top.

### Topology guidelines

From our experience, we have defined a basic "rule of thumb" guide for network topologies, which may help people thinking about potential topology sizes for 5 Mbps networks. Generally, a network which works at 500 kbps using HS-CAN transceivers should be able to work at 2 Mbps with CAN-SIC transceivers. Likewise, a network which works at 2 Mbps with HS-CAN transceivers will generally work at 5 Mbps with CAN-SIC transceivers.

The rationale for this guidance is partly explained earlier in the paper: HS-CAN transceivers at 500 kbps have similar levels of allowable ringing time to CAN-SIC transceivers at 2 Mbps. Likewise, HS-CAN transceivers at 2 Mbps have similar levels of allowable ringing time to CAN-SIC transceivers at 5 Mbps.

Additionally, the available margin for 500 kbps HS-CAN networks allows quite some ringing to occur before the earliest sampling point, which is a similar case with CAN-SIC transceivers at 2 Mbps. At 2 Mbps with HS-CAN transceivers, the ringing needs to quickly be below the 0.5 V to guarantee reliable operation. This same logic also applies to CAN-SIC transceivers, but then at 5 Mbps. Due to the reduced timing margins at 5 Mbps, if CAN Signal Improvement is able to maintain the peak of signal ringing below 0.5 V, this is a strong indicator that the network can operate at 5 Mbps. If the first peak is still above 0.5 V, it is likely that this topology is too severe for this bit rate. Note, however, this still allows a lot of possibilities for topologies to include unterminated stubs, star points, etc.

To give an illustration of what is possible, additional simulations are shown in Figure 6, based on a simple star topology of 4 nodes, with 60 Ohm split star termination, and four unterminated stubs of 2 × 5 m and 2 × 0.75 m. As before, A) shows HS-CAN transceivers operating at 2 Mbps, B) shows CAN-SIC transceivers at 2 Mbps, C) shows HS-CAN transceivers at 5 Mbps and D) shows CAN-SIC transceivers at 5 Mbps. Already in the 2 Mbps simulations, the CAN-SIC transceivers are able to control the ringing sufficiently to bring the first peak below 0.5 V, indicating this topology can reliably operate at 5 Mbps. From the reference simulations A) and C) with HS-CAN transceivers, it is clear this topology is already very challenging.

> Figure 6: Example simulations of HS-CAN and CAN-SIC transceivers in a challenging star topology.

It is important to note that this is not a claim that all networks validated at 500 kbps will work at 2 Mbps with CAN-SIC transceivers; it is possible to find examples violating this guideline. However, as a generic guideline, it sets expectations of what can be realized. This guideline has also been empirically tested by customers and for those that tried with real-world network examples, has been shown correct, but again — this is not an assertion that it is impossible to find a case where this does not hold.

### Sample point selection

The sample point selection at faster bit rates is slightly different compared with the normal sample point selection at slower speeds, e.g. 2 Mbps.

At 2 Mbps, the sample point should be later in the bit to allow maximum time for ringing. This is normally chosen around 70% with standard HS-CAN transceivers but could be delayed even to 80%. We would still recommend this approach of delaying the sample point to boost the available topology space as much as possible and a move to an 80% sample point would provide the maximum time for ringing.

At 5 Mbps however, as noted above, any ringing above the 0.5 V is likely to already touch the boundary of the safe operating area, and so it is no longer necessary to delay the sample point to later in the bit; moving closer to the middle of the bit is preferred to provide additional margin for jitter effects or PCB impacts. With reference to Figure 5 B) and D), moving the sample point earlier at 5 Mbps with CAN-SIC transceivers would move the boundary of the safe operating area earlier and provide additional margin around each of the transitions. As a guideline, we would recommend a sample point of 50% + 1 tq, which is approximately 55%.

Please note, this also applies to the Secondary Sample Point as well, which should be set the same as the normal sample point. Incorrect setting of the Secondary Sample Point is the cause for many support cases of CAN FD networks, providing a latent problem, likely not visible on ECU tests. This issue may never arise if operating at lower bit rates, e.g. 2 Mbps, but for higher bit rates, such as 5 Mbps, this will definitely be encountered. It is therefore vitally important to check the Secondary Sample Point is correctly set to the same as the normal Sample Point when operating at higher speeds.

### Cabling choices

The CiA 601-6 specification provides guidance on creating CAN FD networks and includes the statement in section 8.1.1 that cable impedances should be within 110...140 Ohms. Furthermore, it even gives a cautionary word, "NOTE — PVC-based wire-insulation material does not meet this requirement" [6].

This warning is given due to two effects of the cables, namely a greater sensitivity to temperature that can significantly reduce the impedance of the cable, and a higher propagation delay. The impedance change creates a larger impedance mismatch and so accentuates ringing effects in the network, creating a higher reflection peak; the longer propagation time means that peak would arrive later. Please note, the network simulations shown here are made according to this guidance.

The effect of CAN-SIC transceivers provides some compensation for poorer performing cables however, due to the tighter symmetry, faster recessive edge, plus the Signal Improvement actively drives the signal towards recessive.

Caution is needed however, and the worst-case network simulation defined above would not be sufficient to make this assessment, due to the high temperature dependency of the cable. Also, due to the high variance even across different kinds of PVC cables, it is highly recommended to cross-check the performance of the specific cable to be used over temperature. However, CAN Signal Improvement technology can certainly improve the reach of what is possible and in relatively simple networks, PVC cables may be considered.

## Conclusion

In this paper, we have demonstrated the improvements that are brought about by CAN Signal Improvement, in terms of how it opens the path towards 5 Mbps CAN FD networks, through improved symmetry and its ability to quickly control signal ringing. We are now seeing multiple interested parties working on bringing this to market in the future and are excited to see this expand the offering of CAN FD in the future, based on existing CAN FD controllers and available technology.

There are, of course, possibilities to go beyond 5 Mbps; 8 Mbps is possible in point-to-point networks. However, there are significantly lower returns in terms of net throughput when moving beyond 5 Mbps. The performance improvement from 2 Mbps to 5 Mbps is roughly 43% (based on a 64-byte payload), but from 5 Mbps to 8 Mbps, it is 19%. Doubling the payload size at 5 Mbps would already bring a 26% improvement. Therefore, the work now happening on CAN-XL is a logical progression of the speed increase enabled by CAN Signal Improvement.

However, even with existing available CAN FD controllers, there is a dramatic speed increase to be gained for very practical applications.

## References

- [1] T. Adamson, "Managing the Transition to Robust CAN FD", 16th international CAN Conference Proceedings, Nuremberg, Germany, 2017.
- [2] A. Mutter, "Robustness of a CAN FD Bus System — About Oscillator Tolerance and Edge Deviations", 14th international CAN Conference Proceedings, Paris, France, 2013.
- [3] Dr. M. Schreiner, "CAN FD System Design", 15th international CAN Conference Proceedings, Vienna, Austria, 2015.
- [4] CiA 601 Draft Standard Proposal Part 3: System design recommendation, v1.0.0.
- [5] CiA 601 Draft Standard Proposal Part 4: Signal Improvement, v2.0.0, 16 August 2019.
- [6] CiA 601 Draft Standard Proposal Part 6: CAN FD cable, v1.0.0, 27 June 2019.

## 作者信息

Tony Adamson, NXP Semiconductors, Gerstweg 2, NL-6534AE Nijmegen, www.nxp.com

Axel Engelhard, NXP Semiconductors Germany GmbH, Troplowitzstr. 20, DE-22529 Hamburg, www.nxp.com

Edmund Zhang, NXP Semiconductors, 20F, BM InterContinental Business Center, 100 Yu Tong Road, CN-200070 Shanghai, www.nxp.com
