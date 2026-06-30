# Prompt-Structure Speculative Draft for JSON/Code Generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-structure-speculative-draft-for-json-code-generation-07a0fcfb0d03`
Run ID: `prompt-structure-speculative-draft-for-json-code-generation-07a0fcfb0d03-20260529T105401049197+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5213de7fb002

## What looked useful

The explicit speculative-draft prompt slightly improved the tiny general model overall (9/28 vs 8/28) but hurt JSON there, and on the stronger code-specialized model tied JSON at 14/14 while reducing code success from 10/14 to 8/14 with higher token and latency cost.

## Boundaries and scale limits

Small synthetic benchmark, two Qwen-family local models, greedy decoding only, explicit visible draft text only; not a HumanEval/MBPP/repository-scale benchmark and not evidence about hidden internal reasoning or constrained decoding.

## Claim scope

On a 28-task local benchmark using greedy generation with Qwen/Qwen2.5-0.5B-Instruct and Qwen/Qwen2.5-Coder-1.5B-Instruct, an explicit visible draft-then-final prompt did not robustly improve validated JSON/Python generation versus a direct final-answer prompt.

## Why it stopped

Bounded local evidence is mixed and negative on the stronger code model, so the improvement claim is not robust enough for paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; if deepening, run a bounded ablation comparing direct, explicit draft, final-only checklist, and constrained JSON decoding on MBPP-style code tasks and schema tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-Structure Ablation for Final-Only JSON and Code Generation
- Success threshold: A non-explicit-draft structured variant improves validated success by at least 10 percentage points over direct prompting on both JSON and code subsets for the stronger model, without increasing parse failures or mean generated tokens by more than 25%.
- Stop condition: Stop if explicit draft remains worse than direct on the stronger model and no final-only structured variant beats direct by at least 5 percentage points on either subset.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-structure-speculative-draft-for-json-code-generation-07a0fcfb0d03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
