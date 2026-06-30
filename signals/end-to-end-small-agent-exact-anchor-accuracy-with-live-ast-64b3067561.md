# End-to-end small-agent exact-anchor accuracy with live AST anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `end-to-end-small-agent-exact-anchor-accuracy-with-live-ast-64b3067561`
Run ID: `end-to-end-small-agent-exact-anchor-accuracy-with-live-ast-64b3067561-20260529T033731099828+0000`

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

- Parent run decision: Real-trace exact-anchor replay for small CPU agents: enoch://control-plane/projects/real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41/runs/real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41-20260528T161321080441+0000
- Parent run decision: Prospective live exact-anchor generation for small CPU agents: enoch://control-plane/projects/prospective-live-exact-anchor-generation-for-small-cpu-age-8da4670e30/runs/prospective-live-exact-anchor-generation-for-small-cpu-age-8da4670e30-20260528T213813425586+0000

## What looked useful

Across 1,000 fixed seeds and 96,000 actions per strategy, live qualified AST reached 100.0% exact-anchor accuracy and patch success; definition-grep and live unqualified AST reached 31.5%; stale initial AST reached 14.2%; text-first reached 0.0%. The bounded evidence supports the mechanism that anchors need both live refresh and qualified AST identity.

## Boundaries and scale limits

Synthetic Python only; deterministic resolver rather than a real LLM small-agent loop; truth labels and live resolver both use Python ast semantics; no invalid-syntax intermediate states; no real repository or human-authored task corpus.

## Claim scope

On parseable generated Python modules with repeated method names and multi-step line-shifting edits, resolving anchors by re-parsing the current AST and using the full qualified symbol path achieved exact current AST span selection for every tested action, outperforming definition-grep, live unqualified AST, stale initial AST, and text-first baselines.

## Why it stopped

Bounded synthetic direct metrics support the mechanism but are insufficient for paper readiness because no real small-agent loop or real repository task corpus was validated.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should replay real repository edit traces or a small LLM-agent harness and require live qualified AST to improve exact applied-patch placement over grep and stale-anchor baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-repo small-agent replay of live qualified AST anchors
- Success threshold: At least 500 real edit actions with live qualified AST improving exact applied-patch placement by at least 20 percentage points over the strongest baseline and not increasing parse/test failures.
- Stop condition: Stop if live qualified AST improves by less than 5 percentage points over the strongest baseline after 200 labeled real actions or if invalid-syntax states prevent live AST construction in more than 25% of actions without recoverable fallback.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-agent-exact-anchor-accuracy-with-live-ast-64b3067561`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
