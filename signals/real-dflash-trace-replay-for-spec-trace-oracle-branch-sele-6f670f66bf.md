# Real DFlash Trace Replay for Spec Trace Oracle Branch Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf`
Run ID: `real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf-20260519T235546563709+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Spec Trace Oracle v0 for DFlash Branch Selection: enoch://control-plane/projects/spec-trace-oracle-v0-dflash-branch-selection/runs/spec-trace-oracle-v0-dflash-branch-selection-20260519T235017287435+0000
- ChatGPT Pro unified speculative-decoding trace/oracle plan: file://new-chatgpt-pro-ideas-05-19-more.md
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/abs/2603.03251?utm_source=chatgpt.com
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/abs/2602.13836?utm_source=chatgpt.com
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/abs/2501.10868?utm_source=chatgpt.com
- Spec Trace Oracle v0 for DFlash Branch Selection: https://github.com/z-lab/dflash
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/abs/2503.01840?utm_source=chatgpt.com
- Spec Trace Oracle v0 for DFlash Branch Selection: file://new-chatgpt-pro-ideas-05-19-more.md
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/abs/2411.04975?utm_source=chatgpt.com
- Spec Trace Oracle v0 for DFlash Branch Selection: https://arxiv.org/html/2403.06988v1?utm_source=chatgpt.com

## What looked useful

The 24-prompt held-out run reached 0.9992 of oracle score and 0.9167 oracle branch match with prefix-trace replay, while global replay reached 0.9533 of oracle score but only 0.4167 branch match. The signal supports prefix trace replay as the mechanism worth testing on actual DFlash traces, but it is not paper-ready.

## Boundaries and scale limits

Tested only 24 local short prompts, distilgpt2 draft, gpt2 target, greedy decoding, branch lengths 1/2/4/8, and a fixed synthetic cost model. No DFlash checkpoints, diffusion blocks, production traces, broad prompt distribution, or measured serving latencies were used.

## Claim scope

In a small GPT-2-class direct trace replay test, real draft/target acceptance traces can support near-oracle speculative branch selection when the selector uses an observed k=2 prefix acceptance trace; a global historical replay selector is weaker.

## Why it stopped

Tier 1 direct controlled test completed with useful mechanism evidence but insufficient DFlash-specific and scale evidence for a paper.

## Recommended next action

Run the same held-out replay/oracle evaluation on actual DFlash trace logs or DFlash checkpoints with measured per-branch latencies; stop if prefix replay fails to reach at least 0.95 oracle score on a larger prompt split.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: DFlash checkpoint trace replay with measured branch latency
- Success threshold: Prefix replay reaches >=0.95 held-out oracle score ratio, beats static best-k by >=5% relative score, and has a bootstrap 95% confidence interval lower bound above the static baseline.
- Stop condition: Stop as unsupported if prefix replay is below 0.90 oracle score ratio or does not beat static best-k on the held-out split after measured-latency costs are applied.

## Evidence references

- Artifact root: `<local-path>/projects/real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
