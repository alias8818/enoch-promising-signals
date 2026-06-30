# Spec Trace Oracle v0 for DFlash Branch Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `spec-trace-oracle-v0-dflash-branch-selection`
Run ID: `spec-trace-oracle-v0-dflash-branch-selection-20260519T235017287435+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

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

Trace-derived branch selection improved mean accepted tokens per verification from 0.2428 to 0.2842 in the medium sweep and from 0.1793 to 0.2583 in the noisy-draft control, while reducing regret to a clairvoyant branch selector.

## Boundaries and scale limits

No real DFlash model, LLM target, GPU kernel, KV-cache behavior, or wall-clock decoding throughput was tested. Results are proxy-only synthetic evidence over 5 medium seeds plus 3 noisy-draft control seeds.

## Claim scope

In a deterministic synthetic branch-selection simulator with repeated contexts, an online trace table keyed by context, branch position, and token selected branches with higher accepted-prefix length than draft-logprob and global-frequency baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports a mechanism but does not validate DFlash end-to-end speedup.

## Recommended next action

Run a bounded real-trace replay follow-up by instrumenting a DFlash implementation to log candidate branches and accepted-prefix lengths, then compare trace_oracle_v0 against greedy branch choice on replay and online decode tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real DFlash Trace Replay for Spec Trace Oracle Branch Selection
- Success threshold: Trace oracle improves accepted tokens per verifier call by at least 5% over greedy_logprob and does not reduce wall-clock tokens/sec on a real DFlash decode benchmark.
- Stop condition: Stop if replay improvement is under 2% on two real trace sets or if online decode overhead eliminates the accepted-token gain.

## Evidence references

- Artifact root: `<local-path>/projects/spec-trace-oracle-v0-dflash-branch-selection`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
