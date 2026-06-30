# Local LLM Evidence-Ledger Tool-Use Benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-llm-evidence-ledger-tool-use-benchmark-805e6824d3`
Run ID: `local-llm-evidence-ledger-tool-use-benchmark-805e6824d3-20260609T005606116010+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger Agent Loop with Tiny Tool-Use Sandbox: enoch://control-plane/projects/evidence-ledger-agent-loop-with-tiny-tool-use-sandbox-7156da20fc24/runs/evidence-ledger-agent-loop-with-tiny-tool-use-sandbox-7156da20fc24-20260608T223917957683+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/767958d5e25e

## What looked useful

The evidence-ledger protocol did not meet the Tier 1 success threshold: baseline fully_supported_rate was 1.0, ledger fully_supported_rate was 1.0, and ledger-minus-baseline was 0.0 versus the required +0.10. Ledger prompting increased median latency from 0.897 s to 2.307 s.

## Boundaries and scale limits

Single local 7B-class GGUF model, one seed, simple single-hop lookup tasks, supplied retrieval outputs rather than real tool-call loops, no adversarial multi-hop corpus, no larger model family replication.

## Claim scope

On 24 controlled synthetic retrieval-output tasks with one current document, one superseded archive distractor, and one neighbor distractor, local Qwen2.5-7B-Instruct Q4_K_M achieved identical fully supported answer rate with baseline and evidence-ledger prompts.

## Why it stopped

Tier 1 direct test did not satisfy the stated improvement threshold; this is not a full validation, but it directly falsifies the threshold for the tested simple retrieval-output task family.

## Recommended next action

Stop this run as a scoped negative/useful-signal result; run a bounded harder follow-up with multi-hop or adversarial retrieval outputs where the baseline is not saturated.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Evidence-Ledger Retrieval-Output Benchmark
- Success threshold: ledger fully_supported_rate >= baseline fully_supported_rate + 0.10, invalid JSON rate <= 0.05, and median latency overhead <= 3x baseline on at least 60 tasks
- Stop condition: Stop if baseline remains >=0.95 fully supported on the harder task set or if ledger invalid JSON exceeds 0.20 after one prompt-format repair.

## Evidence references

- Artifact root: `<local-path>/projects/local-llm-evidence-ledger-tool-use-benchmark-805e6824d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
