# Pre-commit counterexample mining on real LLM code-action candidates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pre-commit-counterexample-mining-on-real-llm-code-action-c-877c7a891d`
Run ID: `pre-commit-counterexample-mining-on-real-llm-code-action-c-877c7a891d-20260630T124604272147+0000`

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

- Parent run decision: Counterexample-Mining Step Before Agent Action Commit: enoch://control-plane/projects/counterexample-mining-step-before-agent-action-commit-5e2a791d51f7/runs/counterexample-mining-step-before-agent-action-commit-5e2a791d51f7-20260630T123003136304+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6535d1d4d6f9

## What looked useful

The last-failed-verification gate rejected 22 of 500 candidates with 31.82% unresolved precision versus a 27.2% unresolved base rate, 5.15% unresolved recall, and 4.12% false-reject rate among resolved candidates. The stricter must-verify-after-edit gate had 27.0% precision and 67.58% false-reject rate, showing that naive verification-presence gating mostly rejects valid patches.

## Boundaries and scale limits

Single model/system submission; no rerun of repository pre-commit hooks or benchmark tests; trajectory-derived verification labels only; no multi-submission robustness check.

## Claim scope

On one public SWE-bench bash-only GPT-5.2 high-reasoning submission with 500 real LLM code-action trajectories, simple pre-submit trajectory gates provide at most weak unresolved-candidate enrichment and are not sufficient as standalone pre-commit counterexample miners.

## Why it stopped

Proxy/trajectory-level evidence weakly supports the mechanism but falsifies naive pre-commit gates as paper-worthy standalone counterexample miners.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test richer failure classification across multiple public SWE-bench submissions before considering scale-out.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-submission pre-submit failure taxonomy for LLM code-action counterexample mining
- Success threshold: A pre-submit gate or small rule ensemble reaches at least 60% unresolved precision, at least 10% recall of unresolved candidates, and at most 5% false-reject rate among resolved candidates on held-out submissions.
- Stop condition: Stop if after five submissions no rule exceeds 40% unresolved precision or if false rejects remain above 10% for every rule with at least 10% recall.

## Evidence references

- Artifact root: `<local-path>/projects/pre-commit-counterexample-mining-on-real-llm-code-action-c-877c7a891d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
