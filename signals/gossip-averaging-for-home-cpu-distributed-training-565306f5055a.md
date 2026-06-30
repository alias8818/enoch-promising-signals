# Gossip Averaging for Home CPU Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-for-home-cpu-distributed-training-565306f5055a`
Run ID: `gossip-averaging-for-home-cpu-distributed-training-565306f5055a-20260527T014113270306+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42851e3fbff3

## What looked useful

Gossip averaging at reduced frequency preserved similar accuracy to synchronized baselines while using 27.3% of every-step allreduce bytes, but periodic allreduce every 8 steps used only 12.2% with similar accuracy and local-only was competitive. Future claims must beat periodic allreduce and local-only at matched communication budgets.

## Boundaries and scale limits

No real multi-host WAN, NAT, churn, straggler, packet-loss, or neural/transformer training was tested. The larger 16-worker/4096-dimension matrix was interrupted after 6:47.21 to respect the CPU-worker budget.

## Claim scope

Single-process NumPy simulation of distributed logistic regression with 12 simulated home workers, synthetic non-IID data, 3 seeds, 3 skew levels, and byte/uplink accounting.

## Why it stopped

Proxy/local evidence is mixed and not paper-ready: gossip did not dominate cheaper periodic allreduce or local-only baselines in the tested mechanism setting.

## Recommended next action

Stop this run as a proxy early falsification; only continue with a bounded neural-model follow-up that compares gossip against periodic allreduce and local-only under matched communication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-budget gossip versus periodic allreduce on a small neural model
- Success threshold: Gossip must improve final accuracy by at least 1 percentage point or final loss by at least 10% versus periodic allreduce and local-only at the same communication budget.
- Stop condition: Stop if periodic allreduce or local-only matches gossip within 1 percentage point accuracy and 10% loss at equal or lower communication.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-for-home-cpu-distributed-training-565306f5055a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
