# AdaptiveSpec: Speculative Cascade with Acceptance-Driven Draft Length

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptivespec-speculative-cascade-with-acceptance-driven-draft-length-a3866457e3bf`
Run ID: `adaptivespec-speculative-cascade-with-acceptance-driven-draft-length-a3866457e3bf-20260628T181725862432+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f09155c847f9

## What looked useful

Acceptance-driven draft length is directionally useful under changing acceptance regimes, but this simple cascade controller is not robust enough for a paper claim; AIMD or oracle static controls matched or beat it, and stationary-easy regimes showed about an 8% throughput loss.

## Boundaries and scale limits

Simulation/proxy only: no live LLM target/draft models, no GPU serving kernels, no batching/KV-cache effects, no tokenizer effects, and no direct quality-preservation validation.

## Claim scope

In a local discrete-event speculative decoding latency simulator, a simple EWMA acceptance-driven cascade selector produced small gains over fixed static lookahead in non-stationary regimes, but did not beat the best tuned reference policy in any tested scenario after parameter sensitivity.

## Why it stopped

Proxy simulation and tuning produced an early negative result for the specific EWMA acceptance-driven cascade heuristic rather than publication-grade support.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, test a contextual confidence/entropy-aware controller against AIMD and best static in the same simulator before any real-model benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Contextual Acceptance Controller for Adaptive Speculative Cascade
- Success threshold: Beat AIMD by at least 3% average tokens_per_latency on non-stationary scenarios while losing no more than 1% versus best static/oracle static on stationary scenarios.
- Stop condition: Stop if the contextual controller fails the threshold under the same simulator or if gains depend on oracle-only features unavailable during real decoding.

## Evidence references

- Artifact root: `<local-path>/projects/adaptivespec-speculative-cascade-with-acceptance-driven-draft-length-a3866457e3bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
