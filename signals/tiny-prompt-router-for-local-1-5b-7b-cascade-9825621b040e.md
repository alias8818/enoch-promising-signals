# Tiny Prompt Router for Local 1.5B/7B Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-prompt-router-for-local-1-5b-7b-cascade-9825621b040e`
Run ID: `tiny-prompt-router-for-local-1-5b-7b-cascade-9825621b040e-20260516T212256888625+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/97ffa072f350

## What looked useful

Selective escalation has measurable headroom: held-out all-small pass rate was 0.75, all-large was 0.90, and oracle cascade was 0.95 with 20% large calls. The tested tiny prompt-only router had held-out AUC 0.48 for small-model failure and routed 0% of held-out prompts under calibration, matching all-small at 0.75.

## Boundaries and scale limits

Synthetic coding prompts only; 30 total tasks with 10 calibration and 20 held-out tasks; one deterministic generation per task; not validated on production prompts, non-code workloads, multiple seeds, or larger benchmark suites.

## Claim scope

On a 30-task synthetic Python coding benchmark using local Qwen2.5-Coder-1.5B-Instruct and Qwen2.5-Coder-7B-Instruct, the 7B model improved held-out pass rate over 1.5B, and an oracle cascade could recover additional quality with fewer large calls, but the tested prompt-only logistic router did not generalize.

## Why it stopped

Proxy/local benchmark produced a useful cascade signal but early-falsified the specific tiny prompt-only router mechanism; this is not a full validation of local 1.5B/7B routing.

## Recommended next action

Stop this run as no-paper evidence; run a bounded deepen experiment with richer cheap router signals and locked calibration before held-out scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cheap Confidence Router for Qwen2.5-Coder 1.5B/7B Cascade
- Success threshold: On held-out prompts, achieve at least 90% of the all-large quality gain over all-small while using no more than 40% large-model calls, with improvement over prompt-only and heuristic routers.
- Stop condition: Stop if held-out router AUC for recoverable small-model failures is below 0.60 or if quality-cost improvement over all-small is not positive after locked threshold selection.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-prompt-router-for-local-1-5b-7b-cascade-9825621b040e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
