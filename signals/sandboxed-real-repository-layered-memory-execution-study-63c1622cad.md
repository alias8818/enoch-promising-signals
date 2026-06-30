# Sandboxed Real-Repository Layered Memory Execution Study

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sandboxed-real-repository-layered-memory-execution-study-63c1622cad`
Run ID: `sandboxed-real-repository-layered-memory-execution-study-63c1622cad-20260619T134601405418+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Layered Memory for Repeated Local Agent Tasks: enoch://control-plane/projects/operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023/runs/operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023-20260619T130942112611+0000
- Parent run decision: Real-Agent Layered Memory Compliance Study: enoch://control-plane/projects/real-agent-layered-memory-compliance-study-447157f57f/runs/real-agent-layered-memory-compliance-study-447157f57f-20260619T132958412808+0000

## What looked useful

Corrected full benchmark used fixed seeds 11, 29, and 47 with 1080 paired evaluations per mode. layered_full reached Hit@1 0.7722 and MRR 0.8587 versus flat_content Hit@1 0.1306 and MRR 0.2744; paired Hit@1 delta was +0.6417 with bootstrap 95% CI [0.6130, 0.6694]. Removing the symbol layer reduced Hit@1 to 0.1917, while removing the path layer left Hit@1 at 0.7694, indicating the useful mechanism is mainly symbol/definition memory.

## Boundaries and scale limits

The evidence covers 105 non-test Python files from requests, click, and rich with generated definition-localization tasks. It does not cover open-ended coding, issue repair, LLM-agent behavior, language-server baselines, direct ripgrep exact-search baselines, embedding retrieval, non-Python repositories, or large monorepos.

## Claim scope

On three real public Python repositories, AST-derived symbol/definition memory substantially improved deterministic source-file localization for generated repository-navigation tasks over flat lexical content retrieval, path-only, random, and no-symbol ablation controls.

## Why it stopped

Tier 2 local evidence was achieved with fixed seeds, real repositories, ablations, controls, and a real flat baseline, but the task is generated source-file localization rather than end-to-end repository execution, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepening should test the symbol-memory mechanism on issue-derived or manually written repository tasks against ripgrep, language-server symbol search, flat lexical retrieval, and embedding retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Issue-Derived Repository Tasks for Symbol-Memory Navigation
- Success threshold: Symbol-memory policy improves target-file Hit@3 by at least 15 percentage points over the strongest non-symbol baseline with a paired bootstrap 95% CI excluding zero, without increasing median files-read budget by more than 25%.
- Stop condition: Stop as negative if symbol memory fails to beat the strongest baseline by 5 percentage points Hit@3 or if improvement disappears after removing target-identifier leakage on manually written tasks.

## Evidence references

- Artifact root: `<local-path>/projects/sandboxed-real-repository-layered-memory-execution-study-63c1622cad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
