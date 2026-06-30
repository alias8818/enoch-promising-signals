# Larger frozen held-out replay confirmation for layered doctrine memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `larger-frozen-held-out-replay-confirmation-for-layered-doc-32802d9143`
Run ID: `larger-frozen-held-out-replay-confirmation-for-layered-doc-32802d9143-20260620T155902316461+0000`

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

- Parent run decision: Live Small-Agent Counterexample Mining on Held-Out Replay Tasks: enoch://control-plane/projects/live-small-agent-counterexample-mining-on-held-out-replay-31a1b0a407/runs/live-small-agent-counterexample-mining-on-held-out-replay-31a1b0a407-20260620T152832533205+0000
- Parent run decision: Counterexample-Mining Pipeline for Small CPU Agents: enoch://control-plane/projects/counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba/runs/counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba-20260620T150812130028+0000

## What looked useful

Layered doctrine memory reached 1.000 mean accuracy versus transcript_search 0.884580 and flat_retrieval 0.809190. The shuffled-scope control fell to 0.581516, supporting scoped memory separation, but the no-doctrine-filter ablation reached 0.999036, so the specific doctrine-filter weighting mechanism was not isolated.

## Boundaries and scale limits

The scaffold shipped only a placeholder replay task, so the corpus was generated locally. This does not validate real agent transcript extraction, real operator data, LLM behavior under long-context pressure, or publication-scale robustness.

## Claim scope

In a deterministic synthetic frozen held-out replay corpus with 5 fixed seeds and 5,188 durable-doctrine queries, scoped layered memory recovered the correct operator/project doctrine more accurately than no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

Tier 2 synthetic held-out confirmation produced useful mechanism evidence but not publication-grade direct evidence; real transcript replay remains untested.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should replace the synthetic generator with a frozen real or externally audited replay corpus while keeping the same baselines and shuffled-scope/no-filter controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen real-transcript replay for scoped layered doctrine memory
- Success threshold: Layered doctrine memory must exceed transcript_search and flat_retrieval by at least 8 absolute accuracy points on direct held-out durable doctrine queries, contradiction rate must be below 5%, and shuffled-scope control must be at least 20 points lower than full layered memory.
- Stop condition: Stop as negative if the frozen real replay corpus cannot be assembled without private/raw operator data leakage, or if layered memory fails to clear the accuracy and contradiction thresholds against both real baselines.

## Evidence references

- Artifact root: `<local-path>/projects/larger-frozen-held-out-replay-confirmation-for-layered-doc-32802d9143`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
