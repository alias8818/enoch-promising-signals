# LLM-generated noisy replay validation for predictive memory updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `llm-generated-noisy-replay-validation-for-predictive-memor-49e4be728d`
Run ID: `llm-generated-noisy-replay-validation-for-predictive-memor-49e4be728d-20260614T084222111383+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Realistic replay validation for predictive agent memory updates: enoch://control-plane/projects/realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd/runs/realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd-20260614T065032314542+0000
- Parent run decision: Held-out model-generated replay validation for predictive memory updates: enoch://control-plane/projects/held-out-model-generated-replay-validation-for-predictive-6bbc1f710e/runs/held-out-model-generated-replay-validation-for-predictive-6bbc1f710e-20260614T072730239020+0000

## What looked useful

At the primary 0.40 assistant-noise condition, predictive_memory reached 0.9283 mean accuracy versus 0.8076 for flat_retrieval and 0.7119 for transcript_search. Bootstrap accuracy delta was +0.1207 vs flat_retrieval with 95% CI [+0.1178, +0.1234]. Ablations were weaker, supporting source filtering and recency weighting as active mechanism components.

## Boundaries and scale limits

Replay text was template-generated locally rather than sampled from a deployed LLM or real operator logs; the memory strategy was evaluated in a standalone algorithmic harness, not an integrated agent memory system; no 7B+ model, human labels, or production trace validation was run.

## Claim scope

In deterministic generated repeated-agent replay with noisy assistant conjectures/summaries, user corrections, latent fact drift, 12 fixed seeds, 96 users, 32 sessions, and 8 memory keys, a source-aware and recency-aware predictive memory update rule improved next-session fact prediction over no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

No-paper closure: bounded generated-replay evidence supports the mechanism but is not direct enough for publication-grade validation.

## Recommended next action

Run the same fixed strategy matrix on actual LLM-paraphrased replay traces or real repeated-agent logs with human-checked memory labels before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-paraphrased replay validation for predictive memory updates
- Success threshold: Predictive_memory beats flat_retrieval by at least 5 percentage points in next-session accuracy with a 95% confidence interval lower bound above 0, while not increasing Brier error.
- Stop condition: Stop if predictive_memory fails to beat flat_retrieval by 5 percentage points or if source/recency ablations are indistinguishable from the full method on labeled LLM/real replay traces.

## Evidence references

- Artifact root: `<local-path>/projects/llm-generated-noisy-replay-validation-for-predictive-memor-49e4be728d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
