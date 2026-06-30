# Direct LLM Agent Test for Exact-Anchor Memory Invalidation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-llm-agent-test-for-exact-anchor-memory-invalidation-569185c995`
Run ID: `direct-llm-agent-test-for-exact-anchor-memory-invalidation-569185c995-20260523T230453062888+0000`

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

- Parent run decision: Exact-Anchor Agent Memory Ledger: enoch://control-plane/projects/exact-anchor-agent-memory-ledger-679f7a7192fc/runs/exact-anchor-agent-memory-ledger-679f7a7192fc-20260523T222931438247+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

Exact anchor strings help, but prompt-level direct state maintenance is not reliable enough by itself: main pass rate was 32/36 overall, with exact invalidation only 9/12. A production design should make deletion a deterministic tool/runtime operation rather than relying on the model to rewrite the active ledger perfectly.

## Boundaries and scale limits

Synthetic ledger records, one 7B local instruction model for the main run, 12 fixed-seed cases, immediate single-turn invalidation only, no persistent memory tool/runtime and no frontier hosted model validation.

## Claim scope

In a Tier 1 prompt-level local LLM agent test, Qwen2.5-7B-Instruct Q4_K_M preserved anchored memories under no-op commands and mostly respected near-miss invalidation, but did not reliably produce a coherent post-state for exact deletion of an existing anchor.

## Why it stopped

Tier 1 direct local LLM agent test completed and missed the success threshold: overall pass rate was 0.8889 versus required 0.90, and exact-invalidation pass rate was 0.75 versus required 0.90.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a tool-backed persistent-memory test where the LLM selects an anchor and deterministic code applies invalidation, then persistence is checked after intervening turns.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tool-backed exact-anchor invalidation with persistence checks
- Success threshold: >=0.98 coherent runtime state after deletion and >=0.95 correct post-turn recall/absence across all control conditions, with prompt-only baseline lower by at least 5 percentage points or clearly less coherent.
- Stop condition: Stop if deterministic runtime state is correct but LLM anchor selection or post-turn recall falls below 0.90 in any critical condition, or if prompt-only and tool-backed results are indistinguishable on coherence and persistence.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-agent-test-for-exact-anchor-memory-invalidation-569185c995`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
