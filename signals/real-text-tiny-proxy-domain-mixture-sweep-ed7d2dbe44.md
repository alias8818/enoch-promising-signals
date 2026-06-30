# Real-text tiny proxy domain mixture sweep

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-tiny-proxy-domain-mixture-sweep-ed7d2dbe44`
Run ID: `real-text-tiny-proxy-domain-mixture-sweep-ed7d2dbe44-20260629T211403111791+0000`

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

- Parent run decision: Domain mixture ratio sweep with tiny proxies: enoch://control-plane/projects/domain-mixture-ratio-sweep-with-tiny-proxies-880acfbc2433/runs/domain-mixture-ratio-sweep-with-tiny-proxies-880acfbc2433-20260629T205342054765+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

Target fraction produced a clear target-vs-retention tradeoff. Mean Sci/Tech BPB improved from 2.9900 at 0% target data to 2.6518 at 100% target data, while World/Sports/Business BPB worsened by 0.3446/0.3347/0.1901 respectively.

## Boundaries and scale limits

Proxy-only result: byte-level tiny model, AG News only, two deeper seeds, short fixed token budget, no GPT-2-scale/subword/full-corpus validation, and no downstream task evaluation.

## Claim scope

In a tiny 470,784-parameter byte-level Transformer trained on real AG News text for 12.288M byte-token predictions per mixture fraction, pure Sci/Tech target-domain training achieved the best Sci/Tech validation BPB across two deeper seeds; intermediate mixtures preserved other-domain losses but did not beat target-only on the target objective.

## Why it stopped

Small real-text proxy found no interior mixture that beats target-only for target-domain loss; the result is useful for triage but is not full validation.

## Recommended next action

Stop this worker run as a no-paper useful signal; if continuing, run a bounded GPT-2-small-class subword follow-up that evaluates both target BPB and multi-domain retention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword LM domain-mixture Pareto sweep on AG News
- Success threshold: An intermediate mixture is preferred only if it is within 0.02 BPB of target-only on Sci/Tech while improving mean non-target BPB by at least 0.10, consistently across at least three seeds.
- Stop condition: Stop if target-only beats every intermediate mixture by more than 0.05 Sci/Tech BPB while no intermediate mixture improves mean non-target BPB by at least 0.10.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-tiny-proxy-domain-mixture-sweep-ed7d2dbe44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
