# Physical 5-Device Home LAN Consensus Ledger Validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `physical-5-device-home-lan-consensus-ledger-validation-37d61f7e86`
Run ID: `physical-5-device-home-lan-consensus-ledger-validation-37d61f7e86-20260520T083507284414+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Multi-Agent Consensus Ledger on Home Network: enoch://control-plane/projects/multi-agent-consensus-ledger-on-home-network-1affaf48522d/runs/multi-agent-consensus-ledger-on-home-network-1affaf48522d-20260520T082913280651+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d99004ef738a

## What looked useful

The LAN has many reachable devices, including 56 ping-responsive remote peers and 28 remote peers with SSH-like ports open, but none allowed BatchMode command execution. Reachability is therefore not enough to support the proposed five-device physical ledger validation in this environment.

## Boundaries and scale limits

The probe measured LAN reachability and remote command-execution availability only. It did not run the consensus ledger protocol, measure finality, durability, fork rate, or latency across five physical devices.

## Claim scope

On the current default home LAN from host <lan-ip>, a physical five-device consensus-ledger validation cannot be launched autonomously because only the local host is execution-capable; zero remote LAN peers accepted non-interactive SSH command execution.

## Why it stopped

The controlled direct test failed the minimum five-executor threshold: 1 available executor including self versus 5 required. This is an early deployment-precondition falsification, not a full consensus-ledger validation.

## Recommended next action

Stop this run as a direct Tier 1 cohort-availability failure; rerun only after provisioning four remote LAN peers for passwordless SSH or an equivalent authenticated execution path.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/physical-5-device-home-lan-consensus-ledger-validation-37d61f7e86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
